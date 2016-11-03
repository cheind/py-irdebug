
import numpy as np

from . import diff
from .util import time, state, unpack, mapSignals
from . import sample

def findBursts(sigs, th=15):
    """Automatic detection of signal bursts in signals.
    This method clusters bursts and splits at longer signal pauses. The threshold for
    burst vs. pause is the median of all event intervals times some user specified multiplicative
    factor. 
    """
        
    def _lambda(sig):

        # Create first order differential      
        d = np.diff(state(sig))

        # Get all non zero state ids (events)
        eids = np.where(d != 0)[0] + 1
        eids = np.hstack(([0], eids)) # Add artificial event at zero

        # Compute threshold based on time diffs between events
        dte = np.diff(time(sig)[eids])
        m = np.median(dte)
        myth = m * th
     
        # Add dummy elements to end of list to ensure correct bounds
        eids = np.hstack((eids, [eids[-1]+1]))
        dte = np.hstack((dte, [myth + 1]))
        copy_from = eids[0] if len(eids) > 0 else 0

        b = []
        for i in range(0, len(eids) - 1):
            e0 = eids[i]
            e1 = eids[i+1]            
            if dte[i] > myth:
                if e0 > 0:
                    b.append(sig[copy_from:e0+1])
                copy_from = e1

        return b

    return unpack(mapSignals(sigs, _lambda))