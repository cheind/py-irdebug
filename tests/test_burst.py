from .generate import generateSignal
import numpy as np
import irdebug as ir

def test_findBursts():

    aburst= generateSignal(4,0,0,2)
    s = ir.join([aburst]*3, delay=50)
    b = ir.findBursts(s)

    bz = ir.shiftZero(b)
    np.testing.assert_allclose(bz[0], aburst)
    np.testing.assert_allclose(bz[1], aburst)
    np.testing.assert_allclose(bz[2], aburst)