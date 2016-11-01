import numpy as np
from . import util

def shiftZero(sigs):
    """Shift signal along time axis so that first event happens at zero."""

    def _lambda(sig):
        return sig - np.array([sig[0,0], 0])

    return util.unpack(util.mapSignals(sigs, _lambda))

def shiftOffset(sigs, offset):
    """Shift signal along time axis so that first event happens at zero."""

    def _lambda(sig, offset):
        return sig + np.array([offset, 0])

    return util.unpack(util.mapSignals(sigs, _lambda, offset))
    