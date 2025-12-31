---
title: Flutter app reversing
date: 2025-12-31
slug: flutter-re
tags: solution
...

I've been poking at an Android app written in Flutter, and reverse-engineering it is a bit of a hassle.

Here are the problems I've run into and the solutions I've found.

# 1. Getting the APK(s)
Install the app normally on a rooted phone/emulator and then use `pm path` to find the package files in the  Android filesystem. Fetch them with `adb pull`.

```
#!/bin/bash

PACKAGE=com.company.app

# Locate the APKs on the device
PATHS=( $(adb shell pm path ${PACKAGE} | cut -d ':' -f 2) )

mkdir unmodified
cd unmodified

for P in "${PATHS[@]}"; do
    adb pull "${P}"
done
```

Unpacking the APK will reveal very little of interest, since the app's logic is compiled into `lib/<arch>/libapp.so`.

Opening `libapp.so` in a reversing tool such as Binary Ninja or Ghidra will not reveal much. Strings are there, but no xrefs to them.

Flutter uses Dart, which compiles to its own special kind of binary and follows no common conventions.

# 2. Getting function names
There's an excellent tool called [reflutter](https://github.com/Impact-I/reFlutter) by Impact-I which instruments a Flutter app and uses the Dart runtime (while executing!) to dump information about the program's functions.

This can get you names for most functions in the app, including both application functions and library/runtime stuff.

I use [objection](https://github.com/sensepost/objection) here to repack and resign APKs, but you can use apksigner instead.

The app I'm looking at is distributed as a split APK, and the libapp.so is in `split_config.arm64_v8a.apk` so that's the one that gets patched by reflutter.

```
#!/bin/bash

ORIG_APK_DIR=${1:-${PWD}/../unmodified/}

if [ ! -d "${ORIG_APK_DIR}" ]; then
    echo "reflut.sh <dir-of-unmodified-apks>"
    exit 1
fi

rm *.objection.apk

reflutter --patch-dump ${ORIG_APK_DIR}/split_config.arm64_v8a.apk

cp ${ORIG_APK_DIR}/{base.apk,split_config.en.apk,split_config.sv.apk,split_config.xxhdpi.apk} .
for APK in *.apk; do
    objection signapk $APK
done
```

This should yield a set of files named `*.objection.apk` which are all signed with the same signing key (otherwise they won't install).

```
adb install-multiple *.objection.apk
```

You may get an error like this:
```
Failure [INSTALL_FAILED_UPDATE_INCOMPATIBLE: Package com.miko3.app signatures do not match previously installed version; ignoring!]
```

This is because you're installing new APKs with the same package name as the original app, but you've now signed them with a key that doesn't match the key of the publisher. Android doesn't allow that.

Solution: Uninstall the original app first, then try `adb install-multiple *.objection.apk` again.

Once the reflutter-patched app is installed, run it once. On startup, it will dump a bunch of flutter/dart state to a file. The file is stored in `/data/data/<package-name/dump.dart` on the android device.

```
adb pull /data/data/com.miko3.app/dump.dart
```

You can now parse the `dump.dart` (which isn't actually a dart source file!) and find the names and offsets of functions in `libapp.so`.

If you happen to use Binary Ninja, I've prepared [a script](https://github.com/eldstal/elnino/blob/main/reflutter_load_dump.py) to import `dump.dart` and create/rename functions accordingly.

# 2. Where are all my string xrefs?!

If you are fortunate, your RE tool will have identified a bunch of strings that look relevant (urls, API keys, that sort of thing), but you probably won't see any references to them from the code. That's because Dart uses a weird indirection for its constant storage, so the offsets of the actual strings aren't mentioned directly in the disassembly.

Instead, there will be an instruction sequence like

```
add     x2, x27, #0x15, lsl #0xc
ldr     x2, [x2, #0xf0]
```

i.e. a read from `x27 + 0x15040`. On arm64, x27 is the base register for the "Pointer Pool" (PP), which somehow (don't ask me how) leads to the constant data itself. I haven't learned how to decode the PP and find the path directly, but there is another tool called [blutter](https://github.com/worawit/blutter) by Worawit Wangwarunyoo which can do the work for us. Extract the unmodified APK which contains app.so and run blutter on its directory:

```
python3 /path/to/blutter.py unmodified/split_config.arm64_v8a/lib/arm64-v8a/ blutter/
```

This yields a bunch of interesting files, but the one we need at the moment is `pp.txt` which gives us a flat list of the offsets and objects stored by the PP.

You can parse this list with relative ease, and then figure out a way to import it into your RE tool. Basically, you're looking for accesses relative to `x27`, with some static offset. Take that offset, look it up in pp.txt and you'll find the corresponding object.

I've made [a script](https://github.com/eldstal/elnino/blob/main/blutter_load_pp.py) for binja which imports `pp.txt` and adds comments in the disassembly where a PP access is made as well as xrefs to strings where possible.



# 3. Patching the app
Once you've found function names and some data references, you may be able to start reversing the app. The calling convention used by Dart is utterly confusing to standard RE tools, but you can still probably make some sense of the call graph and string use.

Let's say you found a root detection function and you need to patch an instruction. How do you run the patched app?

It's relatively straight-forward, actually:

1. Modify libapp.so (e.g. change an instruction)
2. Replace libapp.so in the corresponding APK with your patched copy
3. Zipalign and Sign the APK (I use objection because it's easy)
4. Install all the APKs again and you're done!

```
!/bin/bash

# We are in patched/
# and we have already created ./lib/arm64-v8a/libapp.so which is our altered library

cp ../unmodified/*.apk .

# Inject the patched libapp.so into the split_config.arm64_v8a.apk
# The -0 is important here! If you allow the lib to be compressed, it may fail to load.
zip -0 -r split_config.arm64_v8a.apk lib/

for APK in base.apk split_config.en.apk split_config.sv.apk split_config.arm64_v8a.apk split_config.xxhdpi.apk; do
    objection signapk $APK
done

adb install-multiple *.objection.apk
```

You may get an error when installing:
```
INSTALL_FAILED_INVALID_APK: Failed to extract native libraries, res=-2
```

This is due to a new mechanism in android where native libraries can be loaded directly from the APK without being extracted to the device filesystem. This only works if the so is **uncompressed* in the APK (i.e. `store` instead of `deflate` mode). Ensure you've used `-0` for the zip command, or the equivalent when you replace the so file in the APK.


With some luck, the app will run and your patch will work.

Happy hacking!
