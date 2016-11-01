from .generate import generateSignal
import numpy as np
import irdebug as ir


def test_diff():
    s = generateSignal(3, t=0, deltaT=5)
    sd = ir.diff(s)

    assert sd.shape == (2, 2)

    np.testing.assert_allclose(sd, np.array([
        [5, 1],
        [5, -1]
    ]))