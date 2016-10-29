import numpy as np

from . import diff
from . import shift

def join(sigs, intra_pause=0, end_pause=0, shift_signals="never"):
    """Join signals on time axis.
    Time axis needs to be strictly increasing for all signals. 
    You may want to use shift.toZero() to make all signals zero time based first. 
    """

    r = __shift_signals(sigs[0], shift_signals, 0)

    for i in range(1, len(sigs)):        
        r[-1,0] += intra_pause

        s = __shift_signals(sigs[i], shift_signals, i)      
        s = shift.byOffset(s, r[-1,0])
        ss = s[0, 1] == r[-1, 1]
        if ss: # End state equals First state
            r = np.concatenate((r, s[1:,]))
        else:
            r = np.concatenate((r, s))
    
    r[-1,0] += end_pause
    
    return r


def __shift_signals(s, t="never", index=0):
    if t == "first" and index == 0:
        return shift.toZero(s)
    elif t == "all":
        return shift.toZero(s)
    else:
        return s
