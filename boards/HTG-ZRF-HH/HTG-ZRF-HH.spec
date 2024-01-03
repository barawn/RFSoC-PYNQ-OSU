# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

ARCH_HTG-ZRF-HH := aarch64
BSP_HTG-ZRF-HH := HTG-ZRF-HHv1.bsp
BITSTREAM_HTG-ZRF-HH := base/base.bit
FPGA_MANAGER_HTG-ZRF-HH := 1

STAGE4_PACKAGES_HTG-ZRF-HH := pynq xrt ethernet smbus2 
STAGE4_PACKAGES_HTG-ZRF-HH += xrfclk xrfdc rfsystem
STAGE4_PACKAGES_HTG-ZRF-HH += tics
