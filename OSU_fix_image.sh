#!/bin/bash

# The PYNQ build process autograbs
# prebuilt stuff from Xilinx directories.
# The prebuilt portions are pretty big (2 GB)
# so rather than re-host that stuff elsewhere,
# the easy solution is here: we just update
# the files in the image.
#
# We're running in a VM so go sudo crazy
sudo kpartx -av $1
sudo mount /dev/mapper/loop0p2 /mnt
# fix debugbridge
cp pynq/pynq/lib/debugbridge.py /mnt/usr/local/share/pynq-venv/lib/python3.10/site-packages/pynq/lib/
# other fixes go here
sudo umount /mnt
sudo kpartx -d $1
