ARCH_HTG-ZRF-HH := aarch64
# this HAS to be $(BOARD_NAME).bsp
# due to the insanity of the Pynq build system
BSP_HTG-ZRF-HH := HTG-ZRF-HH.bsp
BITSTREAM_HTG-ZRF-HH := base/base.bit
FPGA_MANAGER_HTG-ZRF-HH := 1

STAGE4_PACKAGES_HTG-ZRF-HH := pynq xrt ethernet smbus2 
STAGE4_PACKAGES_HTG-ZRF-HH += xrfclk xrfdc rfsystem
STAGE4_PACKAGES_HTG-ZRF-HH += tics
