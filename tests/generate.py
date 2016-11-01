import numpy as np

def generateSignal(n, t=0, s=0, deltaT=10):
    t = np.arange(t, t + n*deltaT, step=deltaT, dtype=int)
    y = np.empty(t.shape, dtype=int)
    y[::2] = s
    y[1::2] = (s + 1) % 2

    return np.column_stack((t,y))