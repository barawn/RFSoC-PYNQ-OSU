# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

ARCH_SURFv6revB := aarch64
BSP_SURFv6revB := SURFv6revB.bsp
BITSTREAM_SURFv6revB := base/base.bit
FPGA_MANAGER_SURFv6revB := 1
SDBOOT_SURFv6revB := /dev/mmcblk1p2

STAGE4_PACKAGES_SURFv6revB := pynq xrt ethernet smbus2 
STAGE4_PACKAGES_SURFv6revB += xrfclk xrfdc rfsystem

