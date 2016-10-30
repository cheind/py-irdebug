
import numpy as np

from . import diff
from . import util

def detect(sigs, th=15):
    """Automatic detection of signal bursts in signals.
    This method clusters bursts and splits at longer signal pauses. The threshold for
    burst vs. pause is the median of all event intervals times some user specified multiplicative
    factor. 
    """
        
    def __lambda(sig, th):
        d = diff.firstOrder(sig)

        # Use a multiplicative of the median to separate bursts in signal
        m = np.median(d[:,0])
        th = m * th

        labels = np.empty(sig.shape[0], dtype=np.int32)
        label = 0
        labels[0] = label
        for i in range(0, len(d)):
            if d[i,0] > th:
                label += 1                    
            labels[i + 1] = label
            
        nbursts = len(np.unique(labels))
        
        return [sig[np.where(labels==id)[0]] for id in range(0, nbursts)]

    return util.mapSignals(sigs, __lambda, th)