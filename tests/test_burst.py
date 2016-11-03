from .generate import generateSignal
import numpy as np
import irdebug as ir

def test_findBurstsSparse():

    aburst= generateSignal(4,0,0,2)
    s = ir.join([aburst]*3, delay=50)
    b = ir.findBursts(s)

    bz = ir.shiftZero(b)
    np.testing.assert_allclose(bz[0], aburst)
    np.testing.assert_allclose(bz[1], aburst)
    np.testing.assert_allclose(bz[2], aburst)

def test_findBurstsDense():

    aburst = generateSignal(4,0,0,2)
    s = ir.join([aburst]*3, delay=50)
    ss = ir.sampleUniform(s)

    b = ir.findBursts(ss)

    assert len(b) == 3

    bz = ir.shiftZero(ir.sampleSparse(b))
    np.testing.assert_allclose(bz[0], aburst)
    np.testing.assert_allclose(bz[1], aburst)
    np.testing.assert_allclose(bz[2], aburst)


def test_findBurstsPauseAtBeginning():

    s = np.array([
        [0, 0],
        [5, 0],
        [10, 0],
        [15, 0],
        [20, 0],
        [25, 1],
        [30, 0],
        [35, 1],
    ])

    b = ir.findBursts(s, th=1)
    assert len(b) == 1
    np.testing.assert_allclose(b[0], np.array([
        [25, 1],
        [30, 0],
        [35, 1]
    ]))

def test_findBurstsPauseAtEnd():

    s = np.array([
        [0, 0],
        [5, 0],
        [10, 0],
        [15, 0],
        [20, 0],
        [25, 1],
        [30, 0],
        [35, 1],
        [40, 1],
        [40, 1],
        [40, 1],
        [40, 1],
        [40, 1],
        [40, 1],
        [40, 1],
        [40, 1],
    ])

    b = ir.findBursts(s, th=1)
    assert len(b) == 1
    np.testing.assert_allclose(b[0], np.array([
        [25, 1],
        [30, 0],
        [35, 1]
    ]))

def test_findBurstsShort():
    s = np.array([[10, 1]])
    b = ir.findBursts(s, th=1)
    assert len(b) == 0

    s = np.array([[10, 0], [15, 1]])
    b = ir.findBursts(s, th=1)
    np.testing.assert_allclose(b[0], s)
    assert len(b) == 1