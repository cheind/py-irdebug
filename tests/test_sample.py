from .generate import generateSignal
import numpy as np
import irdebug as ir

def test_uniform():
    s = np.array([
        [10,0],[20,1],[25,0]
    ])

    su = ir.sampleUniform(s, start_zero=True)
    np.testing.assert_allclose(su, np.array([
        [0, 1],
        [5, 1],
        [10, 0],
        [15, 0],
        [20, 1],
        [25, 0]
    ]))

    su = ir.sampleUniform(s, start_zero=False)
    np.testing.assert_allclose(su, np.array([
        [10, 0],
        [15, 0],
        [20, 1],
        [25, 0]
    ]))

def test_sparse():
    s = np.array([
        [0, 1],
        [5, 1],
        [10, 0],
        [15, 0],
        [20, 1],
        [25, 0]
    ])

    sp, idx = ir.sampleSparse(s, return_index=True)
    np.testing.assert_allclose(sp, np.array([
        [0, 1],[10,0],[20,1],[25,0]
    ]))
    np.testing.assert_allclose(idx, np.array([0, 2, 4, 5]))