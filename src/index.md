---
pagetitle: Albin Eldstål-Ahrens

...

# Albin Eldstål-Ahrens
Ph.D. Candidate at Chalmers University of Technology, Gothenburg, Sweden.

[Doctoral Defense](/phd)


# Links
[ [GitHub](https://github.com/eldstal) ] |
[ [LuftensHjältar](https://luftenshjaltar.info) ] |
[ [CTFTime](https://ctftime.org/team/50600) ]

# Projects
## Security
### ![strinvader](/strinvader.png) [strinvader](https://github.com/eldstal/strinvader)
_Unicode denormalizer_

Unicode is quite complex. Since there are many different ways to encode the
same text, applications may use _normalization_ to preprocess it into a
predictable form. Strinvader is a tool to find multiple text inputs which
normalize to the same (given) text. This is useful in security research,
because sometimes security features such as block lists are applied to text
_before_ normalization. When attacking such an application, strinvader can
generate a text encoding such as `www.exⓐmple.com` which will pass the block
list and be normalized to `www.example.com` before being used. Interestingly,
normalization rules vary slightly between implementations. Unicode
normalization differs from python's `str.lower()` which differs from the URL
parsing in node.js. For this reason, strinvader contains support for a number
of different such normalization forms.

### ![spike](/spike.png) [spike](https://github.com/eldstal/spike)
_Power glitch generator_

Hardware devices with opaque or protected firmware may still be vulnerable to hardware
faults. One such hardware fault is a _power glitch_, a transient drop in the power feed.
This can have a variety of effects, ranging from device restarts to failure of individual
executed instructions. Spike is a [Zephyr](https://zephyrproject.org/) project for the
Nordic Semiconductor [nRF52840 DK](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk)
development board, which is able to control a target device and perform power glitch
attacks against it.

### ![DESYNK](/desynk.png) [DESYNK](https://github.com/eldstal/desynk)
_Clock glitch generator_

Another hardware fault is caused by an unstable clock signal. Shortening individual
clock cycles can have interesting effects on the instruction decoder/execution stages
of a microprocessor, or adversely affect I/O. DESYNK is a work-in-progress project to
explore this. It is based on the [ICEbreaker](https://1bitsquared.com/products/icebreaker)
development board, powered by the Lattice iCE40UP5k FPGA. DESYNK controls the clock signal
driving the target device, and probes for the proper time and duration of clock inconsistency,
in order to cause interesting software failures.

### ![CTF Notes](/gitbook.png) [CTF Notes](https://luftenshjaltar.gitbook.io/ctf/)
_It won't be a surprise, the second time I see this._

Running notes on CTF techniques, methodology, little tricks we've learned along the way.

## Other
### ![Cardcinogen](/cardcinogen.png) [Cardcinogen](https://github.com/eldstal/cardcinogen)

_Deck generator for [Tabletop Simulator](https://store.steampowered.com/app/286160/Tabletop_Simulator/)_

Cardcinogen is a templating system which allows you to create styles for playing cards and
populate those cards with content from your own data. This is useful to make expansions
for card-based games such as Concept or Fluxx.

### ![Panel of Doom](/pod.png) [Panel of Doom](https://github.com/eldstal/avr-pod)
_DIY USB joystick HID device_

POD uses low-cost commodity components (an AVR ATMEGA-328 microcontroller with no USB hardware support)
to implement a standard joystick. This lets you, for example, build the custom control
panel of your tractor simulation dreams. By using the standard USB HID interface, no
extra drivers or bindings are required to use it in typical PC games. The software USB
stack used in POD is kindly provided by the [V-USB](https://www.obdev.at/products/vusb/index.html)
library.

### ![CTF](ctf.png) [CTF Terminal Frontend](https://github.com/eldstal/CTF)
_Capture-The-Flag scoreboard visualization_

This program queries a live CTF scoreboard and presents the data in your terminal.
Some fun animations are implemented, for example when a team grabs the _first blood_
of one of the challenges. Several popular serverside systems are supported, and the
design is modular to allow for easy addition of new backends
(i.e. support for new online CTF scoreboard systems such as [CTFd](https://ctfd.io/)).


### ![Teksh](/teksh.png) [Teksh](https://github.com/eldstal/teksh)
_Command shell implemented in LaTeX_

The LaTeX typesetting engine wasn't intended for this.


# Security
I've found and reported the following vulnerabilities in software projects:


<div class="nojust">

<!-- [ [CVE-2022-XXXXX](https://www.cvedetails.com/cve/CVE-2022-XXXXX) ] -->
[ [Report](https://github.com/openscad/openscad/issues/4043) ]
([CVSS 4.6](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:L/MI:N/MA:L&version=3.1))
Out-of-bounds read in OpenSCAD (Comment parser)

<!-- [ [CVE-2022-XXXXX](https://www.cvedetails.com/cve/CVE-2022-XXXXX) ] -->
[ [Report](https://github.com/openscad/openscad/issues/4037) ]
([CVSS 4.6](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:L/MI:N/MA:L&version=3.1))
Out-of-bounds read in OpenSCAD (DXF path)

<!-- [ [CVE-2022-XXXXX](https://www.cvedetails.com/cve/CVE-2022-XXXXX) ] -->
[ [Report](https://developer.blender.org/T94661) ]
([CVSS 4.6](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:L/MI:N/MA:L&version=3.1))
Out-of-bounds read in Blender (DDS loader)

<!-- [ [CVE-2022-XXXXX](https://www.cvedetails.com/cve/CVE-2022-XXXXX) ] -->
[ [Report](https://developer.blender.org/T94629) ]
([CVSS 7.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:L/E:U/RL:U/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:H/MI:L/MA:L&version=3.1))
Controlled out-of-bounds read/write in Blender (IMB_flipy)

<!-- [ [CVE-2022-XXXXX](https://www.cvedetails.com/cve/CVE-2022-XXXXX) ] -->
[ [Report](https://developer.blender.org/T94572) ]
([CVSS 5.4](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L/E:U/RL:U/RC:R/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:L/MI:L/MA:L&version=3.1))
Multiple Out-of-bounds reads/writes in Blender (HDR loader)

<!-- [ [CVE-2021-XXXXX](https://www.cvedetails.com/cve/CVE-2021-XXXXX) ] -->
[ [Report](https://github.com/OSGeo/shapelib/issues/39) ]
([CVSS 6.0](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L/E:U/RL:U/RC:R/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:N/MS:C/MC:L/MI:L/MA:L&version=3.1))
Double-Free in shapelib (contrib/shpsort)

<!-- Not yet reported to CVE program, pending confirmation from developer -->
[ [Report](https://github.com/LibreCAD/LibreCAD/issues/1481) ]
([CVSS 4.6](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:L/MI:N/MA:L&version=3.1))
Out-of-bounds read in LibreCAD (importshp DBF parser)

[ [CVE-2021-45847](https://www.cvedetails.com/cve/CVE-2021-45847) ]
[ Report [1](https://github.com/slic3r/Slic3r/issues/5118)
  [2](https://github.com/slic3r/Slic3r/issues/5119)
  [3](https://github.com/slic3r/Slic3r/issues/5120) ]
([CVSS 3.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:N/MI:N/MA:L&version=3.1))
Multiple NULL-pointer dereferences in Slic3r (3MF XML)

[ [CVE-2021-45846](https://www.cvedetails.com/cve/CVE-2021-45846) ]
[ [Report](https://github.com/slic3r/Slic3r/issues/5117) ]
([CVSS 3.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:N/MI:N/MA:L&version=3.1))
NULL-pointer dereference in Slic3r (AMF XML)

[ [CVE-2021-45845](https://www.cvedetails.com/cve/CVE-2021-45845) ]
[ [Report](https://tracker.freecad.org/view.php?id=4810) ]
([CVSS 7.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:L/E:P/RL:W/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:H/MI:H/MA:L&version=3.1))
RCE in FreeCAD (Path Sanity Check script)

[ [CVE-2021-45844](https://www.cvedetails.com/cve/CVE-2021-45844) ]
[ [Report](https://tracker.freecad.org/view.php?id=4809) ]
([CVSS 7.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:L/E:P/RL:W/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:H/MI:H/MA:L&version=3.1))
RCE in FreeCAD (ODA DWG import)

[ [CVE-2021-45343](https://www.cvedetails.com/cve/CVE-2021-45343) ]
[ [Report](https://github.com/LibreCAD/LibreCAD/issues/1468) ]
([CVSS 3.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:N/MI:N/MA:L&version=3.1))
NULL-pointer dereference in LibreCAD (DXF HATCH 93)

[ [CVE-2021-45342](https://www.cvedetails.com/cve/CVE-2021-45342) ]
[ [Report](https://github.com/LibreCAD/LibreCAD/issues/1464) ]
([CVSS 7.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:L/E:P/RL:W/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:H/MI:H/MA:L&version=3.1))
RCE in LibreCAD (JWW CDataList)

[ [CVE-2021-45341](https://www.cvedetails.com/cve/CVE-2021-45341) ]
[ [Report](https://github.com/LibreCAD/LibreCAD/issues/1462) ]
([CVSS 7.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:L/E:P/RL:W/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:H/MI:H/MA:L&version=3.1))
RCE in LibreCAD (JWW CDataMoji)

[ [CVE-2021-45340](https://www.cvedetails.com/cve/CVE-2021-45340) ]
[ Report [1](https://github.com/libsixel/libsixel/issues/51)
  [2](https://github.com/saitoha/libsixel/issues/160) ]
([CVSS 3.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L/E:P/RL:T/RC:C/CR:X/IR:X/AR:X/MAV:L/MAC:L/MPR:N/MUI:R/MS:C/MC:N/MI:N/MA:L&version=3.1))
NULL-pointer dereference in libSIXEL

</div>


# Research and Education

## Publications
The following is a list of my academic publications, to date:

<div class="nojust">

<!-- [ [PDF](https://research.chalmers.se/publication/517203/file/517203_Fulltext.pdf) ] -->
[ [URL](https://research.chalmers.se/publication/528343) ]
Lossy and Lossless Compression Techniques to Improve the Utilization of Memory Bandwidth and Capacity\
**Albin Eldstål-Ahrens**\
Doctoral Thesis, Chalmers University of Technology, 2022

[ [PDF](https://research.chalmers.se/publication/528250/file/528250_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3481641) ]
L2C: Combining Lossy and Lossless Compression on Memory and I/O\
**Albin Eldstål-Ahrens**, Angelos Arelakis, Ioannis Sourdis\
ACM Transactions on Embedded Computing Systems (TECS), 2022

[ [PDF](https://research.chalmers.se/publication/517203/file/517203_Fulltext.pdf) ]
[ [URL](https://research.chalmers.se/publication/517203) ]
Reducing Memory Traffic with Approximate Compression\
**Albin Eldstål-Ahrens**\
Licentiate Thesis, Chalmers University of Technology, 2020

[ [PDF](https://research.chalmers.se/publication/521215/file/521215_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3424668) ]
MemSZ: Squeezing Memory Traffic with Lossy Compression\
**Albin Eldstål-Ahrens**, Ioannis Sourdis\
ACM Transactions on Architecture and Code Optimization (TACO), 2020


[ [PDF](https://research.chalmers.se/publication/512096/file/512096_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3337821.3337824) ]
AVR: Reducing Memory Traffic with Approximate Value Reconstruction\
**Albin Eldstål-Damlin**, Pedro Trancoso, Ioannis Sourdis\
International Conference on Parallel Processing (ICPP), 2019


[ [DOI](https://doi.org/10.1109/VTCSpring.2013.6691881) ]
[ [IEEE](https://ieeexplore.ieee.org/document/6691881) ]
An Improved Model of LTE Random Access Channel\
Evgeny Osipov, Laurynas Riliskis, **Albin Eldstål-Damlin**, Michael Burakov, Mats Nordberg, Min Wang\
IEEE 77th Vehicular Technology Conference, 2013


[ [PDF](https://ltu.diva-portal.org/smash/get/diva2:1029175/FULLTEXT02.pdf) ]
An LTE Random Access Channel Model for Wireless Sensor Network Applications\
Mikael Burakov, **Albin Eldstål-Damlin**\
Master's Thesis, Luleå University of Technology, 2012


[ [PDF](https://www.diva-portal.org/smash/get/diva2:1003393/FULLTEXT01.pdf) ]
A comparison of two modes for AEAD services in wireless sensor networks\
**Albin Eldstål-Damlin**, Laurynas Riliskis\
Technical Report, Luleå University of Technology, 2011

</div>

## Supervision
I've had the pleasure of being the advisor for the following Bacherlor's thesis work:

[ [PDF](https://odr.chalmers.se/bitstream/20.500.12380/300034/1/CSE%2019-09%20CPL%20Yngvesson%20Magnusson.pdf) ]
[ [URL](https://hdl.handle.net/20.500.12380/300034) ]
Augmented Reality\
Johan Yngvesson, Johannes Magnusson\
Bachelor's Thesis, Chalmers University of Technology, 2019



## Peer Review
I've served as a reviewer for paper(s) for the following venues:

Computing Frontiers (CF) 2021

Design, Automation and Test in Europe (DATE) 2021

International Conference on Embedded Computer Systems: Architectures, Modeling and Simulation (SAMOS) 2021

Design, Automation and Test in Europe (DATE) 2020

Defect and Fault Tolerance in VLSI and Nanotechnology Systems (DFTS) 2020

Latin American Symposium on Circuits and Systems (LASCAS) 2020

Design, Automation and Test in Europe (DATE) 2019

Transactions on Architecture and Code Optimization (TACO) 2018

Field-Programmable Logic and Applications (FPL) 2017

International Symposium on Computer Architecture (ISCA) 2016

Highly Efficient Accelerators and Reconfigurable Technologies (HEART) 2016

Design, Automation and Test in Europe (DATE) 2016

