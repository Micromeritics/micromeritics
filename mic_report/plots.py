"""This module contains helper functions to show plots."""

import numpy as np
import pylab as pl

def isoplot( Q, P, descr, min=None, max=None ): 
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

def betplot( P, T, slope, y_intercept, max ):
    """Show a BET transform plot wutht he line of best fit overlaid. """

    pl.figure()
    pl.plot( P, T, 'ro' )
    pl.title('BET Surface Area Plot')
    pl.ylabel('$1/[Q(p^\circ/p-1)]$')
    pl.xlabel('Relative Pressure($p/p^\circ$)')

    X = np.array([0.0, max])
    Y = slope*X + y_intercept
    pl.plot( X,Y, 'r-' )
    pl.show()
