# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

ARCH_TEB0835 := aarch64
BSP_TEB0835 := TEB0835.bsp
BITSTREAM_TEB0835 := base/base.bit
FPGA_MANAGER_TEB0835 := 1

STAGE4_PACKAGES_TEB0835 := pynq xrt ethernet smbus2 
STAGE4_PACKAGES_TEB0835 += xrfclk xrfdc rfsystem
STAGE4_PACKAGES_TEB0835 += tics
