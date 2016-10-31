import numpy as np
from . import util

def toZero(sigs):
    """Shift signal along time axis so that first event happens at zero."""

    def __lambda(sig):
        return sig - np.array([sig[0,0], 0])

    return util.unpack(util.mapSignals(sigs, __lambda))

def byOffset(sigs, offset):
    """Shift signal along time axis so that first event happens at zero."""

    def __lambda(sig, offset):
        return sig + np.array([offset, 0])

    return util.unpack(util.mapSignals(sigs, __lambda, offset))
    