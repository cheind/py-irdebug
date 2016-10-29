import numpy as np

def toZero(sigs):
    """Shift signal along time axis so that first event happens at zero."""
    if (isinstance(sigs, list)):
        return [__toZero(s) for s in sigs]
    else:
        return __toZero(sigs)

def byOffset(sigs, offset):
    """Shift signal along time axis so that first event happens at zero."""
    if (isinstance(sigs, list)):
        return [__byOffset(s, offset) for s in sigs]
    else:
        return __byOffset(sigs, offset)

def __toZero(sig):
    return sig - np.array([sig[0,0], 0])

def __byOffset(sig, offset):
    return sig + np.array([offset, 0])