---
title: Albin Eldstål-Ahrens
date: 2025-03-02
slug: index
save_as: index.html
...


<div class="h1" markdown="1">
Offensive Security Certified Professional (OSCP)  
Ph.D. of Computer Science and Engineering, Chalmers University of Technology, Gothenburg, Sweden.

</div>

<div class="h1" markdown="1">


# Links
[ [GitHub](https://github.com/eldstal) ] |
[ [LuftensHjältar](https://luftenshjaltar.info) ] |
[ [CTFTime](https://ctftime.org/team/50600) ] |
[ <a rel="me" href="https://kolektiva.social/@albin">Mastodon</a> ]

</div>

<div class="h1" markdown="1">
# Projects

<div class="h2" markdown="1">
## Security

<div class="h3 project" markdown="1">
### ![MacDongler](/images/macdongler.png) [MacDongler](https://github.com/eldstal/MacDongler)
USB skeleton Key

Some devices (tablet kiosks, buses, cars, air planes, advertising displays, ...) expose
a USB interface, either for user device charging or for development access or both. One
way to lock these devices down is to limit the accepted USB devices, based on model or type
or vendor ID. MacDongler is a scanner based on Linux USB Gadgets, which emulates a large
number of USB devices and automatically determines which ones are accepted by a host. It
can emulate network interfaces, serial ports, HID devices, and more!
</div>


<div class="h3 project" markdown="1">
### ![strinvader](/images/strinvader.png) [strinvader](https://github.com/eldstal/strinvader)
Unicode denormalizer

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
</div>


<div class="h3 project" markdown="1">
### ![spike](/images/spike.png) [spike](https://github.com/eldstal/spike)
Power glitch generator

Hardware devices with opaque or protected firmware may still be vulnerable to hardware
faults. One such hardware fault is a _power glitch_, a transient drop in the power feed.
This can have a variety of effects, ranging from device restarts to failure of individual
executed instructions. Spike is a [Zephyr](https://zephyrproject.org/) project for the
Nordic Semiconductor [nRF52840 DK](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk)
development board, which is able to control a target device and perform power glitch
attacks against it.
</div>


<div class="h3 project" markdown="1">
### ![DESYNK](/images/desynk.png) [DESYNK](https://github.com/eldstal/desynk)
Clock glitch generator

Another hardware fault is caused by an unstable clock signal. Shortening individual
clock cycles can have interesting effects on the instruction decoder/execution stages
of a microprocessor, or adversely affect I/O. DESYNK is a work-in-progress project to
explore this. It is based on the [ICEbreaker](https://1bitsquared.com/products/icebreaker)
development board, powered by the Lattice iCE40UP5k FPGA. DESYNK controls the clock signal
driving the target device, and probes for the proper time and duration of clock inconsistency,
in order to cause interesting software failures.
</div>


<div class="h3 project" markdown="1">
### ![elnino](/images/elnino.png) [elnino](https://github.com/eldstal/elnino)
Scripts for [binary ninja](https://binary.ninja)

A collection of utilities for the binja reverse engineering tool.
</div>


<div class="h3 project" markdown="1">
### ![mediafuzz](/images/mediafuzz.png) [mediafuzz](https://github.com/eldstal/mediafuzz)
Fuzzer for the media metadata display of your car

A small web application which fuzzes the artist/title/album information of your "currently playing"
notification. Run it on your phone and stream the audio by bluetooth to your target device. Hosted [here](/mediafuzz) for your convenience.
</div>


<div class="h3 project" markdown="1">
### ![CTF Notes](/images/gitbook.png) [CTF Notes](https://luftenshjaltar.gitbook.io/ctf/)
It won't be a surprise, the second time I see this.

Running notes on CTF techniques, methodology, little tricks we've learned along the way.
</div>

</div>


<div class="h2" markdown="1">
## Nostalgica

<div class="h3 project" markdown="1">
### ![widelan](/images/widelan.png) [WideLAN](https://gitlab.com/eldstal/widelan)
"Clientless" LAN over the Internet

WideLAN is a set of scripts that make it easy to set up bridging and tunneling over WireGuard
to connect your cool retro gaming VMs to your friends. Crucially, nothing needs to be installed
inside the VMs - all of the tunneling magic is handled by the host system.
</div>

</div>


<div class="h2" markdown="1">
## Other

<div class="h3 project" markdown="1">
### ![touchlaess](/images/touchlaess.png) [Touchlaess XM](https://github.com/eldstal/touchless-xm)
Physical buttons for an otherwise great headset

Sony's WH1000 series headphones are quite good. I really like my pair of XM4, apart from the one
annoying detail of touch controls. Touchlæss XM is a drop-in replacement for the right-hand side earcup
cover, which gives you five (or more!) physical buttons to control volume, play/pause, song skipping
and more. I use it daily, and it works well!
</div>


<div class="h3 project" markdown="1">
### ![replacement-parts](/images/replacement-parts.png) [Replacement-parts.net](https://replacement-parts.net)
An open repository of CAD drawings for old computers and game consoles

So you've got an old Sega Mega Drive II, but the dust flaps covering the cartridge port are broken and jammed half-way open. You could remove them entirely, sure. But maybe someone has made models so you can 3D print new ones? But the printable sites are pretty difficult to search, and the metadata isn't great. Well *look no further*, this is a repository of spare parts organized by machine and part number.
</div>

<div class="h3 project" markdown="1">
### ![nobbler](/images/nobbler.png) [Nobbler](https://github.com/eldstal/nobbler)
Smart Knob Interface

An attempt at a PC-side control loop for the gorgeous [Smartknob](https://github.com/scottbez1/smartknob)
designed by Scott Bez. Nobbler lets you automatically activate different
views on the Smartknob based on system activity (e.g. which window you
have focused) and perform useful tasks when the knob is fiddled with (e.g.
run a command to change system volume, emulate a keypress, ...). 
</div>


<div class="h3 project" markdown="1">
### ![Cardcinogen](/images/cardcinogen.png) [Cardcinogen](https://github.com/eldstal/cardcinogen)
Deck generator for [Tabletop Simulator](https://store.steampowered.com/app/286160/Tabletop_Simulator/)

Cardcinogen is a templating system which allows you to create styles for playing cards and
populate those cards with content from your own data. This is useful to make expansions
for card-based games such as Concept or Fluxx.
</div>


<div class="h3 project" markdown="1">
### ![Panel of Doom](/images/pod.png) [Panel of Doom](https://github.com/eldstal/avr-pod)
DIY USB joystick HID device

POD uses low-cost commodity components (an AVR ATMEGA-328 microcontroller with no USB hardware support)
to implement a standard joystick. This lets you, for example, build the custom control
panel of your tractor simulation dreams. By using the standard USB HID interface, no
extra drivers or bindings are required to use it in typical PC games. The software USB
stack used in POD is kindly provided by the [V-USB](https://www.obdev.at/products/vusb/index.html)
library.
</div>


<div class="h3 project" markdown="1">
### ![CTF](/images/ctf.png) [CTF Terminal Frontend](https://github.com/eldstal/CTF)
Capture-The-Flag scoreboard visualization

This program queries a live CTF scoreboard and presents the data in your terminal.
Some fun animations are implemented, for example when a team grabs the _first blood_
of one of the challenges. Several popular serverside systems are supported, and the
design is modular to allow for easy addition of new backends
(i.e. support for new online CTF scoreboard systems such as [CTFd](https://ctfd.io/)).
</div>



<div class="h3 project" markdown="1">
### ![Teksh](/images/teksh.png) [Teksh](https://github.com/eldstal/teksh)
Command shell implemented in LaTeX

The LaTeX typesetting engine wasn't intended for this.
</div>
</div>

</div>
<div class="h1" markdown="1">
# Security
I am the holder of an [Offensive Security Certified Professional (OSCP)](https://www.credential.net/43d80588-74b1-4d6b-b25e-45078ae452c8) certification.

I've also earned the certification [Red Team Ops I](https://training.zeropointsecurity.co.uk/courses/red-team-ops) issued by Zero Point Security.


I've found and reported the following vulnerabilities in software projects:


{! cve.md !}


</div>
<div class="h1" markdown="1">
# Bugs for Charity
Via bug bounty programs, I've generated $500 for charity. By matching funds, Google VRP has generously
provided an additional $500 of donations.

These donations have been made to the [National Network of Abortion Funds](https://abortionfunds.org).

</div>
<div class="h1" markdown="1">
# Research and Education

<div class="h2" markdown="1">
## Publications
The following is a list of my academic publications, to date:

<div class="nojust" markdown="1">

[ [PDF](https://dl.acm.org/doi/pdf/10.1145/3559009.3569653) ]
[ [DOI](https://doi.org/10.1145/3559009.3569653) ]
FlatPack: Flexible Compaction of Compressed Memory  
**Albin Eldstål-Ahrens**, Angelos Arelakis, Ioannis Sourdis  
International Conference on Parallel Architectures and Compilation Techniques (PACT), 2022

[ [PDF](https://research.chalmers.se/publication/528343/file/528343_fulltext.pdf) ]
[ [URL](https://research.chalmers.se/publication/528343) ]
Lossy and Lossless Compression Techniques to Improve the Utilization of Memory Bandwidth and Capacity  
**Albin Eldstål-Ahrens**  
Doctoral Thesis, Chalmers University of Technology, 2022

[ [PDF](https://research.chalmers.se/publication/528812/file/528812_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3481641) ]
L2C: Combining Lossy and Lossless Compression on Memory and I/O  
**Albin Eldstål-Ahrens**, Angelos Arelakis, Ioannis Sourdis  
ACM Transactions on Embedded Computing Systems (TECS), 2022

[ [PDF](https://research.chalmers.se/publication/517203/file/517203_Fulltext.pdf) ]
[ [URL](https://research.chalmers.se/publication/517203) ]
Reducing Memory Traffic with Approximate Compression  
**Albin Eldstål-Ahrens**  
Licentiate Thesis, Chalmers University of Technology, 2020

[ [PDF](https://research.chalmers.se/publication/521215/file/521215_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3424668) ]
MemSZ: Squeezing Memory Traffic with Lossy Compression  
**Albin Eldstål-Ahrens**, Ioannis Sourdis  
ACM Transactions on Architecture and Code Optimization (TACO), 2020

[ [PDF](https://research.chalmers.se/publication/512096/file/512096_Fulltext.pdf) ]
[ [DOI](https://doi.org/10.1145/3337821.3337824) ]
AVR: Reducing Memory Traffic with Approximate Value Reconstruction  
**Albin Eldstål-Damlin**, Pedro Trancoso, Ioannis Sourdis  
International Conference on Parallel Processing (ICPP), 2019

[ [DOI](https://doi.org/10.1109/VTCSpring.2013.6691881) ]
[ [IEEE](https://ieeexplore.ieee.org/document/6691881) ]
An Improved Model of LTE Random Access Channel  
Evgeny Osipov, Laurynas Riliskis, **Albin Eldstål-Damlin**, Michael Burakov, Mats Nordberg, Min Wang  
IEEE 77th Vehicular Technology Conference, 2013

[ [PDF](https://ltu.diva-portal.org/smash/get/diva2:1029175/FULLTEXT02.pdf) ]
An LTE Random Access Channel Model for Wireless Sensor Network Applications  
Mikael Burakov, **Albin Eldstål-Damlin**  
Master's Thesis, Luleå University of Technology, 2012

[ [PDF](https://www.diva-portal.org/smash/get/diva2:1003393/FULLTEXT01.pdf) ]
A comparison of two modes for AEAD services in wireless sensor networks  
**Albin Eldstål-Damlin**, Laurynas Riliskis  
Technical Report, Luleå University of Technology, 2011

</div>

</div>
<div class="h2" markdown="1">
## Supervision
I've had the pleasure of being the advisor for the following Bachelor's thesis work:

[ [PDF](https://odr.chalmers.se/bitstream/20.500.12380/300034/1/CSE%2019-09%20CPL%20Yngvesson%20Magnusson.pdf) ]
[ [URL](https://hdl.handle.net/20.500.12380/300034) ]
Augmented Reality  
Johan Yngvesson, Johannes Magnusson  
Bachelor's Thesis, Chalmers University of Technology, 2019



</div>
<div class="h2" markdown="1">
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

</div>
</div>
