# B84-4001

The B84-4001 keyboard PCB is a replacement PCB that makes use of the G84-4001's layout, switches, and keycaps and puts them into a subjectively more usable form. It was originally created as a personal project to make use of a new-old-stock controller-less G84 module (a G84-4001QAU/00).

It is for the 83-key models only, though support for G84 variants with Windows keys may be added in future.

![top](/Pictures/top.jpg)
<img src="/Pictures/beauty_shot.jpg" width="640">

I will gladly assist or give tips on assembly, firmware or use (you can find me on Discord as `bean#7178`), but please first read this README through.

This board is designed for Cherry ML switches in 18mm spacing, mounted directly onto the PCB; ML does not use a plate to hold the switches. The PCB has M2 mount holes along the perimeter, allowing one to make it into a sandwich case with another PCB as the baseplate or mount into a custom case. This is **will not fit** in Cherry G84 keyboard cases - it is meant as a standalone keyboard.

### Controller and Firmware

This board uses an [RP2040 ItsyBitsy](https://www.adafruit.com/product/4888) from Adafruit as the keyboard controller, and the firmware is written in [KMK](https://github.com/KMKfw/kmk_firmware). It should be compatible with any other ItsyBitsy, including the 32u4 variant, but I've yet to try and there may be some tweaks to KMK needed for those (and of course for the 32u4, a port to TMK/QMK).

### Assembly

I will not describe in excess detail how to solder or bend your leads here; there is no dearth of soldering tutorials on the internet. What I *will* describe is the order of operations and some extra bits of advice.

1.  Assemble your parts. Simple enough, hopefully.
2.  Solder those diodes! 
	* You will notice there are two sides to the PCB, a side **with** silkscreen and a side without. The side **with** silkscreen is the side from which you will insert the diodes - although the pads are also on the other, silkscreen-less side, do not put the diodes on that side unless you wish to have your keycaps bottom out 2 millimetres early.
	* Once the diodes are soldered, use a pair of flush-cutters to clip the diode legs as close to the PCB as possible, again because of keycap clearance.
