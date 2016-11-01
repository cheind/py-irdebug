import numpy as np
from functools import reduce
import math

from .util import *

def sampleUniform(sigs, ignore_offset=False):

    step = None
    def __gcd(sig):
        return reduce(lambda x,y: math.gcd(x,y), sig[:,0])

    step = reduce(lambda x,y: math.gcd(x,y), mapSignals(sigs, __gcd))

    def __lambda(sig, step):

        t = np.array([], dtype=int)
        y = np.array([], dtype=int)

        first = 0 if ignore_offset else -1
        for i in range(first, sig.shape[0]-1):
            ts,ys = None, None
            if i == -1:
                # Sample from zero to first
                ts = np.arange(0, sig[0,0], step, dtype=int)
                ys = np.full(ts.shape, (sig[0,1] + 1) % 2, dtype=int)
            else:
                # Sample between two events
                ts = np.arange(sig[i,0], sig[i+1,0], step, dtype=int)
                ys = np.full(ts.shape, sig[i,1], dtype=int)
            t = np.concatenate((t, ts), axis=0)
            y = np.concatenate((y, ys), axis=0)

        m = np.column_stack((t, y))   
        # Add last row (not interpolated)   
        return np.vstack((m, sig[-1,:]))      

    return unpack(mapSignals(sigs, __lambda, step))

def sampleSparse(sigs, ignore_offset=False, return_index=False):

    def __lambda(sig):
        # Compare every element to its neighbor and add 1 to correct index
        ids = np.where(sig[:-1, 1] != sig[1:,1])[0] + 1
        if not ignore_offset:
            ids = np.insert(ids, 0, 0)
        e = sig[ids, :]
        return (e, ids) if return_index else e


    return unpack(mapSignals(sigs, __lambda))

def sampleFrequency(sigs, unit=1e6):
    return unpack(mapSignals(sigs, lambda sig: (time(sig)[1] - time(sig)[0])*unit))