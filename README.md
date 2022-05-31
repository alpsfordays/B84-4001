# B84-4001

The B84-4001 keyboard PCB is a replacement (rejuvenation? revival?) PCB that makes use of the G84-4001's layout, switches, and keycaps and puts them into a subjectively more usable form. It was originally created as a personal project to make use of a new-old-stock controller-less G84 module (a G84-4001QAU/00).

It supports one layout, the 83-key layout used by the aforementioned modules, though support for G84 variants with Windows keys may be added in future.

![top](/Pictures/top.jpg)
<img src="/Pictures/beauty_shot.jpg" width="640">

I will gladly assist or give tips on assembly, firmware or use (you can find me on Discord as `bean#7178`), but please first read this README through.

This board is designed for Cherry ML switches in 18mm spacing, mounted directly onto the PCB; ML does not use a plate to hold the switches. The PCB has M2 mount holes along the perimeter, allowing one to make it into a sandwich case with another PCB as the backplate or mount into a custom case. This is **will not fit** in Cherry G84 keyboard cases - it is meant as a standalone keyboard.

I ordered revision zero with green soldermask, 0.8 millimetre with HASL. Revision one (what this repo is) has had its edges tidied up and excess silkscreen reference markings removed. When ordering, I highly recommend *not* specifying 0.8mm thickness - the stock PCB is 1.6mm so I recommend that. Of all the colours I could have chosen, I went for green. You have the gift of hindsight, so do not do what I did and pair the colours grey and bright green.

### Controller and Firmware

This board uses an [RP2040 ItsyBitsy](https://www.adafruit.com/product/4888) from Adafruit as the keyboard controller, and the firmware is written in [KMK](https://github.com/KMKfw/kmk_firmware). It should be compatible with any other ItsyBitsy, including the 32u4 variant, but I've yet to try and there may be some tweaks to KMK needed for those (and of course for the 32u4, a port to TMK/QMK).

### Assembly

I will not describe in excess detail how to solder or bend your leads here; there is no dearth of soldering tutorials on the internet. What I *will* describe is the order of operations and some extra bits of advice.

1.  Assemble your parts. Simple enough, hopefully.
	* 83 Cherry ML switches
	* 83 1N4148 diodes, through-hole or SMD
	* An RP2040 ItsyBitsy
	* Keycaps
	* Stabilizer inserts
	* (for sandwich casing) M2\*8 standoffs and M2\*3 screws, rubber feet and a second PCB

2.  Solder the diodes
	* Basic enough, bend diodes to match the holes, and put the cathode side to the square pads.
	* You will notice there are two sides to the PCB, a side **with** silkscreen and a side without. The side **with** silkscreen is the side from which you will insert or place the diodes - although the pads are also on the other, silkscreen-less side, do not put the diodes on that side unless you wish to have your keycaps bottom out 2 millimetres early.
	* <img src="/Pictures/diodes.jpg" width="640">
	* Once the diodes are soldered, use a pair of flush-cutters to clip the diode legs as close to the PCB as possible, again because of keycap clearance. Note in the image above that when viewing the PCB from the silkscreen-less side; there should be no diodes visible and the legs should be cut flush or as close to flush as possible. 

3.  Solder the headers.
	* Solder the headers, again on the silkscreen side. Clip the headers to be flush or as close to flush as possible on the silkscreen-less side.

4.  Solder the adorably small switches.
	* Now take your ML switches and solder them in - insert them from the silkscreen-less side and get to work melting metal onto those pins. 

5.  Solder the ItsyBitsy.
	* Test that KMK works on the ItsyBitsy, then solder it in as well, component-side facing away from the PCB.

> For sandwich casing, install the standoffs and screw it all together using the second PCB as a backplate. Install rubber feet as desired.

6.  Test and use.
	* Make sure the keys work correctly and all register. Customize the firmware to suit your needs, though of course note that the matrix's representation in the firmware is reversed because... things (I'm lazy). That it works is what matters to me.
	* Install the stabilizer inserts and keycaps (and a touch of lube on the stabilizer wires to taste).

### Licenses

All the software in this repository is licensed under the [GNU Public License,
version 3](https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)).
All the hardware designs and documentation is licensed under the [Creative Commons
Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
license. 
