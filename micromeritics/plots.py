"""This module contains helper functions to show plots."""

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

def plotIsotherm( Q, P, descr, min=None, max=None ): 
    """Show an isotherm plot.  If the min and/or max is available, also show 
    blur bars at those locations."""
    
    pl.figure()
    pl.plot( P, Q, 'ro' )
    pl.title(descr)
    pl.ylabel('Volume Adsorbed (cm^3/g STP)')
    pl.xlabel('Relative Pressure')
    pl.ylim(0,None)
    if min != None : 
        pl.axvline(x=min, color='b')
    if max != None : 
        pl.axvline(x=max, color='b')
    pl.show()

def plotBET( P, T, slope, y_intercept, max ):
    """Show a BET transform plot with the line of best fit overlaid. """

    pl.figure()
    pl.plot( P, T, 'ro' )
    pl.title('BET Surface Area Plot')
    pl.ylabel('$1/[Q(p^\circ/p-1)]$')
    pl.xlabel('Relative Pressure($p/p^\circ$)')

    X = np.array([0.0, max])
    Y = slope*X + y_intercept
    pl.plot( X,Y, 'r-' )
    pl.show()

def plotRouquerol( P, R ) : 
    """Show a Rouquerol BET transform plot. """
    pl.figure()
    pl.plot( P, T, 'ro' )
    pl.title('Rouquerol BET')
    pl.ylabel('$Q(1-p/p^\circ)]$')
    pl.xlabel('Relative Pressure($p/p^\circ$)')

    X = np.array([0.0, max])
    Y = slope*X + y_intercept
    pl.plot( X,Y, 'r-' )
    pl.show()

def plotThickness( P, T, title ):
    """Show a plot of the passed in thickness"""
    fig = plt.figure(figsize=(12,6))
    axes = fig.add_subplot(111)
    axes.plot(P, T, '8', markerfacecolor = 'blue', markersize = 7)
    axes.set_title(title)
    axes.set_xlabel('Relative Pressure')
    axes.set_ylabel('Thickness (A)')
    axes.grid()
    plt.show()
    
