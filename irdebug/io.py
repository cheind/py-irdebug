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
const uint32_t timestamps[] = {{
{}
}};

const uint32_t NEVENTS = {};
""".format(",\n".join(values), sig.shape[0])
    
    with open(filename, "w") as f:
        f.write(content)