# This file handles the base overlay.

import os
os.environ['BOARD'] = 'SURFv6'
import xrfclk
import rfsystem
from smbus2 import SMBus, i2c_msg
import pynq
import pynq.lib
from .constants import *

class BaseOverlay(pynq.Overlay):
    """ Base overlay. Right now do nothing. Figure this stuff out later.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_loaded():
            # uh whatever

