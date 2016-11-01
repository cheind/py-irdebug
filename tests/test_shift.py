from .generate import generateSignal
import numpy as np
import irdebug as ir


def test_shiftZero():
    s0 = generateSignal(2, t=0, deltaT=1)
    s1 = generateSignal(2, t=1, deltaT=1)    
    s = ir.shiftZero((s0,s1))

    np.testing.assert_allclose(s[0], s0)
    np.testing.assert_allclose(s[1], np.array([
        [0, 0],
        [1, 1]
    ]))

def test_shiftOffset():
    s0 = generateSignal(2, t=0, deltaT=1)
    s1 = generateSignal(2, t=-10, deltaT=1)    
    s = ir.shiftOffset((s0,s1), 10)

    np.testing.assert_allclose(s[0], np.array([
        [10, 0],
        [11, 1]
    ]))

    np.testing.assert_allclose(s[1], np.array([
        [0, 0],
        [1, 1]
    ]))