import numpy as np
from scipy import interpolate
from functools import reduce
import math

from . import util

def uniform(sigs):

    step = None
    def __gcd(sig):
        return reduce(lambda x,y: math.gcd(x,y), sig[:,0])

    step = reduce(lambda x,y: math.gcd(x,y), util.mapSignals(sigs, __gcd))

    def __lambda(sig, step):

        f = interpolate.interp1d(sig[:,0], sig[:,1], kind='zero')

        t = np.array([])
        y = np.array([])
        for i in range(0,sig.shape[0]-1):
            ts = np.arange(sig[i,0], sig[i+1,0], step, dtype=int)
            ys = f(ts)
            t = np.concatenate((t, ts))
            y = np.concatenate((y, ys))
        
        return np.column_stack((t, y))

    return util.unpack(util.mapSignals(sigs, __lambda, step)), step
