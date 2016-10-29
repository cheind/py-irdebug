import numpy as np


def firstOrder(sigs):
    """Compute the discrete first order forward differential of signal.
    
    For each element in sig the diff is computed as result[n] = sig[n+1] - sig[n]
    The resulting array has len(sig) - 1.

    Differential is computed for time axis and state axis.
    """
    if (isinstance(sigs, list)):
        return [__firstOrder(s) for s in sigs]
    else:
        return __firstOrder(sigs)
    
def __firstOrder(sig)
    return np.diff(sig, axis=0)