
import numpy as np

from . import diff

def detect(sig, th=15):
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