"""This module contains helper functions to show plots."""

import numpy as np
import tplot
import matplotlib.pyplot as plt

_AXIS_LABEL_QUANTADS = 'Quantity Adsorbed (cm^3/g STP)'
_AXIS_LABEL_RELPRESS = 'Relative Pressure($p/p^\circ$)'
_AXIS_LABEL_ABSPRESS = 'Absolute Pressure (mmHg)'
_AXIS_LABEL_THICKNESS = 'Thickness (A)'

def plotIsotherm( P, Q, descr ): 
    """Show an isotherm plot."""
    
    plt.figure()
    plt.plot( P, Q, 'ro' )
    plt.title(descr)
    plt.ylabel(_AXIS_LABEL_QUANTADS)
    plt.xlabel(_AXIS_LABEL_RELPRESS)
    plt.ylim(0,None)

def addRangeBars( min, max ):
    """Show blue vertical range bars at specified positions"""
    plt.axvline(x=min, color='b')
    plt.axvline(x=max, color='b')

def setXLog():
    """Set the X axis to logarithmic"""
    plt.gca().set_xscale('log')

def setXLinear():
    """Set the X axis to linear"""
    plt.gca().set_xscale('linear')

def setYLog():
    """Set the Y axis to logarithmic"""
    plt.gca().set_yscale('log')

def setYLinear():
    """Set the Y axis to linear"""
    plt.gca().set_yscale('linear')

def show():
    """Show the plots"""
    plt.show()

def plotLangmuirTransform(lang_touple):
    """Show the Langmuir transform plot with the line of best fit overlaid."""

    data = lang_touple
    
    plt.figure()
    plt.plot( data.Pabs_fit, data.transform_fit, 'ro' )
    plt.title('Langmuir Surface Area Plot')
    plt.ylabel('$P/Q$')
    plt.xlabel(_AXIS_LABEL_ABSPRESS)

    X = np.array([0.0, data.Pmax])
    Y = data.line_fit.slope*X + data.line_fit.y_intercept
    plt.plot( X,Y, 'r-' )

def plotLangmuirIsotherm( lang_touple ):
    """Show the Isotherm data with the Langmuir model isotherm overlaid.
    If flog = true show the x-axis as a log scale."""

    data = lang_touple

    # Plot the collected isotherm data
    plt.figure()
    plt.plot( data.Pabs_all, data.Qads_all, 'ro' )
    plt.title('Langmuir Isotherm Plot')
    plt.ylabel(_AXIS_LABEL_QUANTADS)
    plt.xlabel(_AXIS_LABEL_ABSPRESS)

    # Plot the Langmuir Model Isotherm data
    plt.plot( data.Pabs_all, data.Qads_model, 'r-' )

def plotBETTransform( bet_touple ):
    """Show a BET transform plot with the line of best fit overlaid. """

    data = bet_touple

    plt.figure()
    plt.plot( data.Prel_fit, data.transform_fit, 'ro' )
    plt.title('BET Surface Area Plot')
    plt.ylabel('$1/[Q(p^\circ/p-1)]$')
    plt.xlabel(_AXIS_LABEL_RELPRESS)

    X = np.array([0.0, data.Pmax])
    Y = data.line_fit.slope*X + data.line_fit.y_intercept
    plt.plot( X,Y, 'r-' )

def plotBETIsotherm( bet_touple ):
    """Show the Isotherm data with the BET model isotherm overlaid. """

    data = bet_touple

    # Plot the collected isotherm data
    plt.figure()
    plt.plot( data.Prel_all, data.Qads_all, 'ro' )
    plt.title('BET Isotherm Plot')
    plt.ylabel(_AXIS_LABEL_QUANTADS)
    plt.xlabel(_AXIS_LABEL_RELPRESS)

    # Plot the BET Model Isotherm data
    plt.plot( data.Prel_all, data.Qads_model, 'r-' )

def plotRouquerol( P, R ) : 
    """Show a Rouquerol BET transform plot. """
    plt.figure()
    plt.plot( P, T, 'ro' )
    plt.title('Rouquerol BET')
    plt.ylabel('$Q(1-p/p^\circ)]$')
    plt.xlabel(_AXIS_LABEL_RELPRESS)

    X = np.array([0.0, max])
    Y = slope*X + y_intercept
    plt.plot( X,Y, 'r-' )

def plotThickness( P, T, title ):
    """Show a plot of the passed in thickness"""
    fig = plt.figure(figsize=(12,6))
    axes = fig.add_subplot(111)
    axes.plot(P, T, '8', markerfacecolor = 'blue', markersize = 7)
    axes.set_title(title)
    axes.set_xlabel(_AXIS_LABEL_RELPRESS)
    axes.set_ylabel(_AXIS_LABEL_THICKNESS)
    axes.grid()
    
def plotTPlot( tplot_touple ):
    """Show a t-plot with the line of best fit overlaid. """

    data = tplot_touple

    # Create the graph, axes and title
    plt.figure()
    plt.title('T Plot')
    plt.ylabel(_AXIS_LABEL_QUANTADS)
    plt.xlabel(_AXIS_LABEL_THICKNESS)

    # Add quantity adsorbed vs. Thickness curve
    plt.plot( data.t_all, data.Qads_all, 'ro' )

    # Add the linear overlay
    X = np.array([0.0, data.t_all[-1]])
    Y = data.line_fit.slope*X + data.line_fit.y_intercept
    plt.plot( X,Y, 'r-' )

    # Add range bars
    plt.axvline(x=data.tmin, color='b')
    plt.axvline(x=data.tmax, color='b')

