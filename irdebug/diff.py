import numpy as np

from . import util


def diff(sigs, order=1):
    """Compute the discrete n-th order forward differential of signal (time and state domain).
    
    For each element in sig the diff is computed as result[n] = sig[n+1] - sig[n]
    The resulting array has len(sig) - 1. Higher order diffs are computed recursively.

    Differential is computed for time axis and state axis.
    """

    def _diff(sig):
        return np.diff(sig, n=order, axis=0)

    return util.unpack(util.mapSignals(sigs, _diff))
