
from .generate import generateSignal
import numpy as np

def test_generate():
    s = generateSignal(3, t=1, s=1, deltaT=5)
    np.testing.assert_allclose(s, np.array([[1,1],[6,0],[11,1]]))