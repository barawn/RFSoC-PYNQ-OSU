# This file handles the base overlay.

import os
os.environ['BOARD'] = 'HTG-ZRF-HH'
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

    """ RF clock initialization. Figure this out later.
    """
    def init_rf_clks(self, lmk_freq=245.76, lmx_freq=491.52):
        # this is how it's done in the 4x2, ZCU208, etc.
        #xrfclk.set_ref_clks(lmk_freq=lmk_freq, lmx_freq=lmx_freq)
        # xrfclk should be able to handle the HTG as well
        # with minor changes.
