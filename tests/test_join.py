from .generate import generateSignal
import numpy as np
import irdebug as ir


def test_join():
    s0 = generateSignal(5, t=0, deltaT=10, s=0)
    s1 = generateSignal(5, t=1, deltaT=5, s=0)

    s00 = s0.copy()
    s11 = s1.copy()

    s = ir.join((s0, s1), delay=100)
    
    np.testing.assert_allclose(s0, s00)
    np.testing.assert_allclose(s1, s11)
    
    np.testing.assert_allclose(s, np.array([
        [0,0],
        [10,1],
        [20,0],
        [30,1],
        [40,0],
        [146,1],
        [151,0],
        [156,1],
        [161,0]
    ]))
