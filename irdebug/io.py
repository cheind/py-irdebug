import numpy as np

def loadCSV(filename):
    """Load digital signal from file"""
    return np.loadtxt(filename, dtype=int)

def saveCSV(filename, sig):
    """Save digital signal to file"""
    np.savetxt(filename, sig, fmt="%d", header="Time(us) State(High/Low)")

def saveHeader(filename, sig):

    values = [str(e) for e in sig[:,0]]
    values.append("0") # Dummy element added for arduino program

    content = """
// This file is generated by IR Debug utilities for Python.
// https://github.com/cheind/py-irdebug

// A list of events specified as timestamps in microseconds.
const uint32_t timestamps[] = {{
{}
}};

// Number of events (minus one)
const uint32_t NEVENTS = {};

// Initial state of system
const uint8_t ISTATE = {};
""".format(",\n".join(values), sig.shape[0], sig[0,1])
    
    with open(filename, "w") as f:
        f.write(content)