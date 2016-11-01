import numpy as np


def isSignal(x):
    return isinstance(x, np.ndarray) and x.ndim == 2

def isListOfSignals(x):
    return isinstance(x, (list, tuple)) and all([isinstance(e, np.ndarray) for e in x])

def mapSignals(x, fnc, *fnc_args, **fnc_kwargs):
    
    def invoke(x, fnc, *fnc_args, **fnc_kwargs):
        pos = len(fnc_args) > 0
        kw = len(fnc_kwargs) > 0

        if pos and kw:
            return fnc(x, *fnc_args, **fnc_kwargs)
        elif pos and not kw:
            return fnc(x, *fnc_args)
        elif not pos and kw:
            return fnc(x, **fnc_kwargs)
        else:
            return fnc(x)

    if isSignal(x):
        return [invoke(x, fnc, *fnc_args, **fnc_kwargs)]
    elif isListOfSignals(x):
        return [invoke(s, fnc, *fnc_args, **fnc_kwargs) for s in x]
    else:
        raise TypeError("Signal input must be array-like or array of array-like.")

def unpack(x):
    return x if len(x) > 1 else x[0]

def time(sigs):
    return unpack(mapSignals(sigs, lambda sig: sig[:,0]))

def state(sigs):
    return unpack(mapSignals(sigs, lambda sig: sig[:,1]))