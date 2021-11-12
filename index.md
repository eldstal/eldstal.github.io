---
pagetitle: Albin Eldstål-Ahrens

...


# Links
[ [GitHub](https://github.com/eldstal) ] |
[ [LuftensHjältar](https://luftenshjaltar.info) ] |
[ [CTFTime](https://ctftime.org/team/50600) ]

# Resumé
[ [PDF](/cv.pdf) ]

# Projects
## Security
### [strinvader](https://github.com/eldstal/strinvader)
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

### [spike](https://github.com/eldstal/spike)
_Power glitch generator_

Hardware devices with opaque or protected firmware may still be vulnerable to hardware
faults. One such hardware fault is a _power glitch_, a transient drop in the power feed.
This can have a variety of effects, ranging from device restarts to failure of individual
executed instructions. Spike is a [Zephyr](https://zephyrproject.org/) project for the
Nordic Semiconductor [nRF52840 DK](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk)
development board, which is able to control a target device and perform power glitch
attacks against it.

### [desynk](https://github.com/eldstal/desynk)
_Clock glitch generator_

Another hardware fault is caused by an unstable clock signal. Shortening individual
clock cycles can have interesting effects on the instruction decoder/execution stages
of a microprocessor, or adversely affect I/O. Desynk is a work-in-progress project to
exploire this. It is based on the [ICEbreaker](https://1bitsquared.com/products/icebreaker)
development board, powered by the Lattice iCE40UP5k FPGA. Desynk controls the clock signal
driving the target device, and probes for the proper time and duration of clock inconsistency,
in order to cause interesting software failures.

### [CTF Notes](https://luftenshjaltar.gitbook.io/ctf/)
_It won't be a surprise, the second time I see this._

Running notes on CTF techniques, methodology, little tricks we've learned along the way.

## Other
### [Cardcinogen](https://github.com/eldstal/cardcinogen)

_Deck generator for [Tabletop Simulator](https://store.steampowered.com/app/286160/Tabletop_Simulator/)_

Cardcinogen is a templating system which allows you to create styles for playing cards and
populate those cards with content from your own data. This is useful to make expansions
for card-based games such as Concept or Fluxx.

### [Panel of Doom](https://github.com/eldstal/avr-pod)
_DIY USB joystick HID device_

POD uses low-cost commodity components (an AVR ATMEGA-328 microcontroller with no USB hardware support)
to implement a standard joystick. This lets you, for example, build the custom control
panel of your tractor simulation dreams. By using the standard USB HID interface, no
extra drivers or bindings are required to use it in typical PC games. The software USB
stack used in POD is kindly provided by the [V-USB](https://www.obdev.at/products/vusb/index.html)
library.

### [CTF Terminal Frontend](https://github.com/eldstal/CTF)
_Capture-The-Flag scoreboard visualization_

This program queries a live CTF scoreboard and presents the data in your terminal.
Some fun animations are implemented, for example when a team grabs the _first blood_
of one of the challenges. Several popular serverside systems are supported, and the
design is modular to allow for easy addition of new backends
(i.e. support for new online CTF scoreboard systems such as [CTFd](https://ctfd.io/)).


### [Teksh](https://github.com/eldstal/teksh)
_Command shell implemented in LaTeX_

The LaTeX typesetting engine wasn't intended for this purpose.


# Research and Education

## Publications


L2C: Combining Lossy and Lossless Compression onMemory and I/O\
**Albin Eldstål-Damlin**, Angelos Arelakis, Ioannis Sourdis\
ACM Transactions on Embedded Computing Systems, 2021


[ [PDF](https://research.chalmers.se/publication/521215/file/521215_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3424668) ]
MemSZ: Squeezing Memory Traffic with Lossy Compression\
**Albin Eldstål-Damlin**, Ioannis Sourdis\
ACM Transactions on Architecture and Code Optimization (TACO), 2020


[ [PDF](https://research.chalmers.se/publication/512096/file/512096_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3337821.3337824) ]
AVR: Reducing memory traffic with approximate value reconstruction\
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



## Supervision

[ [PDF](https://odr.chalmers.se/bitstream/20.500.12380/300034/1/CSE%2019-09%20CPL%20Yngvesson%20Magnusson.pdf) ]
[ [URL](https://hdl.handle.net/20.500.12380/300034) ]
Augmented Reality\
Johan Yngvesson, Johannes Magnusson\
Bachelor's Thesis, Chalmers University of Technology, 2019



## Peer Review

Design, Automation and Test in Europe (DATE) 2016

Highly Efficient Accelerators and Reconfigurable Technologies (HEART) 2016

International Symposium on Computer Architecture (ISCA) 2016

Field-Programmable Logic and Applications (FPL) 2017

Transactions on Architecture and Code Optimization (TACO) 2018

Design, Automation and Test in Europe (DATE) 2019

Latin American Symposium on Circuits and Systems (LASCAS) 2020

Defect and Fault Tolerance in VLSI and Nanotechnology Systems (DFTS) 2020

Design, Automation and Test in Europe (DATE) 2020

International Conference on Embedded Computer Systems: Architectures, Modeling and Simulation (SAMOS) 2021

Design, Automation and Test in Europe (DATE) 2021

Computing Frontiers (CF) 2021


