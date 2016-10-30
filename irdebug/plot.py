
import numpy as np
import matplotlib.pyplot as pyplot

from . import util

def plot(sigs, plt=None):
    if not plt:
        plt = pyplot

    plt.xlabel("Time $us$")
    plt.ylabel("State")

    def __lambda(sig, plt):        
        plt.step(sig[:,0], sig[:,1], where='post')

    util.mapSignals(sigs, __lambda, plt)        
    plt.ylim(-0.5, 1.5)
