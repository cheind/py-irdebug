import numpy as np

from .util import *

def correlate(sigs, t, normalize=True):

    # Note, we normalize by sum(t) for binary signals
    # That way perfect matches end up at exactly 1
    n = 1.0 / np.sum(t) if normalize else 1
    def _lambda(sig, t, n):        
        return np.correlate(state(sig), state(t), mode="valid") * n

    return unpack(mapSignals(sigs, _lambda, t))