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
    print(step)

    def __lambda(sig, step):

        f = interpolate.interp1d(sig[:,0], sig[:,1], kind='zero', assume_sorted=True)

        t = np.array([], dtype=int)
        y = np.array([], dtype=int)
        for i in range(0, sig.shape[0]-1):
            ts = np.arange(sig[i,0], sig[i+1,0], step, dtype=int)
            ys = f(ts).astype(int)
            t = np.concatenate((t, ts), axis=0)
            y = np.concatenate((y, ys), axis=0)
        # Add last row (not interpolated)    
        m = np.column_stack((t, y))    
        return np.vstack((m, sig[-1,:]))      

    return util.unpack(util.mapSignals(sigs, __lambda, step))

def sparse(sigs):

    def __lambda(sig):
        # Compare every element to its neighbor and add 1 to correct index
        ids = np.where(sig[:-1, 1] != sig[1:,1])[0] + 1
        return np.vstack((sig[0,:], sig[ids, :]))


    return util.unpack(util.mapSignals(sigs, __lambda))