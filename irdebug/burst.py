
import numpy as np

from . import diff
from . import util
from . import sample

def findBursts(sigs, th=15, ignore_offset=False):
    """Automatic detection of signal bursts in signals.
    This method clusters bursts and splits at longer signal pauses. The threshold for
    burst vs. pause is the median of all event intervals times some user specified multiplicative
    factor. 
    """
        
    def _lambda(sig):
        sparse, ids = sample.sampleSparse(sig, ignore_offset, return_index=True)

        # Use a multiplicative of median event arrival times to separate bursts in signal
        d = diff.diff(sparse)
        m = np.median(d[:,0])
        myth = m * th

        # classify
        sids = np.where(d[:,0] > myth)[0]

        # map back to input signal ids
        cids = ids[sids + 1]

        # Issue here: when sigs is already densly sampled we have a lot of trailing 
        # elements that shouldn't be there
        return np.array_split(sig, cids)

    return util.unpack(util.mapSignals(sigs, _lambda))