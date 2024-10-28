FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " file://bsp.cfg"
KERNEL_FEATURES:append = " bsp.cfg"
SRC_URI += "file://surf_user.cfg \
            file://0001-backport-DCC-uart-serialization-option.patch \
            file://0001-add-partial-readback-support.patch \
            file://user_2024-10-04-14-15-00.cfg \
            file://user_2024-10-04-16-28-00.cfg \
            file://user_2024-10-04-17-01-00.cfg \
            file://user_2024-10-15-14-47-00.cfg \
            file://user_2024-10-16-13-51-00.cfg \
            "

