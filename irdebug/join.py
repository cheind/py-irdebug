import numpy as np

from . import diff
from . import shift

def join(sigs, delay=0, shift_signals="never"):
    """Join signals on time axis.
    Time axis needs to be strictly increasing for all signals. 
    You may want to use shift.toZero() to make all signals zero time based first
    or set `shift_signals="always"`
    """

    r = __shift_signals(sigs[0], shift_signals, 0)

    for i in range(1, len(sigs)):        
        s = __shift_signals(sigs[i], shift_signals, i)      
        s = shift.shiftOffset(s, r[-1,0] + delay)
        if s[0, 1] == r[-1, 1]: # End state equals First state
            r = np.concatenate((r, s[1:,]))
        else:
            r = np.concatenate((r, s))

    return r


def __shift_signals(s, t="never", index=0):
    """Helper function to shift based on type string."""
    if t == "first" and index == 0:
        return shift.shiftZero(s)
    elif t == "always":
        return shift.shiftZero(s)
    else:
        return np.copy(s)
