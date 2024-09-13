![](rfsocpynq_logo.png)

# Ohio State modifications

* Add HTG-ZRF-HH, TEB0835, SURFv6/SURFv6revB/SURFv6revBG3 board.
* (in Pynq submodule) - fix Vagrant file so it actually works by adding i386 architecture.
* (in Pynq submodule) - fix DebugBridge instance so it works on Python and not just Jupyter
* (in Pynq submodule) - change build system so that a board-specific variable (SDBOOT_boardname) can be used to specify the location of the root filesystem
* (in Pynq submodule) - fix setup_host.sh so it tries to fetch qemu from the proper URL (god I hate these people)

Note: The Pynq submodule contains a Vagrant file to spin up a virtual machine. You need to use this. Don't try to do any of these directions in a base
operating system! It won't work and it's not safe. This means you need to check this out somewhere with a bucket-ton of space (hundreds of GB free). If you're on Windows
you'll end up needing a complete second installation of Vivado (because OF COURSE). On Linux you can be ultra-clever and mount the external installation
as a shared folder inside the VM but it NEEDS TO BE IN THE SAME LOCATION inside the VM. You'll need to figure out how to use the license inside the VM.
You're bright, you can figure it out.

Again - DO NOT try to follow these instructions in your host operating system.

The PYNQ repositories themselves aren't very well maintained or supported (the Vagrant file fix in the OSU
commit is mentioned __in a comment on the commit__ ). I'll try to backport stuff from there but these
might just end up being a local fork.

## Vagrant/Virtualbox just dies on me!

Yeah. I know. There was some kernel fix that blew up VirtualBox versions pre-7 recently, and many
of the distros still have it, I guess. I don't know the details, I just know you probably need to
upgrade *both* Vagrant *and* VirtualBox using their upstream apt repositories on Ubuntu.

See https://developer.hashicorp.com/vagrant/install
and https://www.virtualbox.org/wiki/Linux_Downloads

## Shouldn't you submit these changes to upstream?

Are you kidding me? The only changes they've made in over a year are to
update a few internal links. The setup_hosts script mistake has been there
forever. No one there cares, if there even is anyone there at all.

## I'm so happy I found this: can you help me with this non-PUEO thing?

No.

## Building

```
make BOARD=(board name)
```
like ZCU111, HTG-ZRF-HH.

__After the build__, you need to run OSU_fix_image.sh (image name) to __actually__ update files in the image. PYNQ
actually grabs prebuilt images from Xilinx's website and they're ~2 GB, so I don't feel like rehosting it. Just easier
for now to selectively replace the files that get edited.

# Original README starts here

This repository contains the source code and build scripts for the RFSoC-PYNQ base design and SD card images. The design files in this repository are compatible with Xilinx Vivado 2022.1, and PYNQ v3.0.0 and later.  

Currently, the ZCU111, ZCU208, RFSoC4x2 and RFSoC2x2 platforms are supported.

## Getting started

Visit the [RFSoC-PYNQ webpage](https://www.rfsoc-pynq.io/) for complete documentation on boards supported, features unique to RFSoC platforms and how to get support.


## Image rebuilding steps

For optional image rebuilding for any of the boards, you will need a Linux (Ubuntu 18.04/20.04) host machine, with Vivado and Petalinux 2022.1 installed. For more host setup instructions please see the PYNQ [sdbuild readme](https://github.com/Xilinx/PYNQ/tree/master/sdbuild).


1. Clone this repository
	
	```bash
	git clone --recursive https://github.com/Xilinx/RFSoC-PYNQ.git
	```

1. Copy the BSP (board support package) into the appropriate board folder.

	| Board  | BSP Link |
	| ------------- | ------------- |
	| ZCU111  | [xilinx-zcu111-v2022.1.bsp](https://www.xilinx.com/member/forms/download/xef.html?filename=xilinx-zcu111-v2022.1-04191534.bsp)  |
	| ZCU208  | [xilinx-zcu208-v2022.1.bsp](https://www.xilinx.com/member/forms/download/xef.html?filename=xilinx-zcu208-v2022.1-04191534.bsp)  |
	| RFSoC4x2  | [RFSoC4x2_2022_1.bsp](https://github.com/RealDigitalOrg/RFSoC4x2-BSP/blob/master/bsp_releases/RFSoC4x2_2022_1.bsp?raw=true)  |
	| RFSoC2x2  | No BSP needed.  |
	
	```
	cp <local-path-to-bsp> boards/<BOARD>/<BOARD>.bsp
	```

3. To rebuild just the base overlay, run
	
	```
	make BOARD=<BOARD> base
	```
4. To rebuild the SD card image, run
	
	```
	make BOARD=<BOARD> image
	```
---
Copyright (C) 2022 Xilinx, Inc

SPDX-License-Identifier: BSD-3-Clause

