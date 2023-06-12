---
pagetitle: Albin Eldstål-Ahrens

...

# Albin Eldstål-Ahrens
Offensive Security Certified Professional (OSCP)\
Ph.D. of Computer Science and Engineering, Chalmers University of Technology, Gothenburg, Sweden.



# Links
[ [GitHub](https://github.com/eldstal) ] |
[ [LuftensHjältar](https://luftenshjaltar.info) ] |
[ [CTFTime](https://ctftime.org/team/50600) ] |
[ <a rel="me" href="https://kolektiva.social/@albin">Mastodon</a> ]

# Projects
## Security

### ![MacDongler](/macdongler.png) [MacDongler](https://github.com/eldstal/MacDongler)
_USB Skeleton Key_

Some devices (tablet kiosks, buses, cars, air planes, advertising displays, ...) expose
a USB interface, either for user device charging or for development access or both. One
way to lock these devices down is to limit the accepted USB devices, based on model or type
or vendor ID. MacDongler is a scanner based on Linux USB Gadgets, which emulates a large
number of USB devices and automatically determines which ones are accepted by a host. It
can emulate network interfaces, serial ports, HID devices, and more!

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

### ![elnino](/elnino.png) [elnino](https://github.com/eldstal/elnino)
_Scripts for [binary ninja](https://binary.ninja)_

A collection of utilities for the binja reverse engineering tool.

### ![mediafuzz](/mediafuzz.png) [mediafuzz](https://github.com/eldstal/mediafuzz)
_Fuzzer for the media metadata display of your car_

A small web application which fuzzes the artist/title/album information of your "currently playing"
notification. Run it on your phone and stream the audio by bluetooth to your target device. Hosted [here](/mediafuzz) for your convenience.

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
I am the holder of an [Offensive Security Certified Professional (OSCP)](https://www.credential.net/43d80588-74b1-4d6b-b25e-45078ae452c8) certification.


I've found and reported the following vulnerabilities in software projects:


$(include "cve.md")


# Bugs for Charity
Via bug bounty programs, I've generated $500 for charity. By matching funds, Google VRP has generously
provided an additional $500 of donations.

These donations have been made to the [National Network of Abortion Funds](https://abortionfunds.org).

# Research and Education

## Publications
The following is a list of my academic publications, to date:

<div class="nojust">

[ [PDF](https://dl.acm.org/doi/pdf/10.1145/3559009.3569653) ]
[ [DOI](https://doi.org/10.1145/3559009.3569653) ]
FlatPack: Flexible Compaction of Compressed Memory\
**Albin Eldstål-Ahrens**, Angelos Arelakis, Ioannis Sourdis\
International Conference on Parallel Architectures and Compilation Techniques (PACT), 2022

[ [PDF](https://research.chalmers.se/publication/528343/file/528343_fulltext.pdf) ]
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
I've had the pleasure of being the advisor for the following Bachelor's thesis work:

[ [PDF](https://odr.chalmers.se/bitstream/20.500.12380/300034/1/CSE%2019-09%20CPL%20Yngvesson%20Magnusson.pdf) ]
[ [URL](https://hdl.handle.net/20.500.12380/300034) ]
Augmented Reality\
Johan Yngvesson, Johannes Magnusson\
Bachelor's Thesis, Chalmers University of Technology, 2019



## Peer Review
I've served as a reviewer for paper(s) for the following publications and conferences:

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

