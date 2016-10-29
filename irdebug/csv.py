import numpy as np

def load(filename):
    """Load digital signal from file"""
    return np.loadtxt(filename, dtype=int)

def save(filename, signal):
    """Save digital signal to file"""
    np.savetxt(filename, signal, fmt="%d", header="Time(us) State(High/Low)")

