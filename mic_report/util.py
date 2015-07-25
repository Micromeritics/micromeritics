import numpy as np
import math

def make_touple( name, **args ) :
    """Make a named touple with the keyword aruments passed in.  

    For example: 
       p = make_touple(x=1.0, y=2.0)
       distance = math.sqrt(p.x**2 + p.y**2)
    """
    from collections import namedtuple
    return namedtuple(name, args.keys() )(**args)

def restrict_isotherm( Qads, Prel, min, max ):
    """Restrict the isother Qads, Prel to relatve pressures between min and max. 

    Returns:  Restrictes Qads, Prel
    """

    b = np.logical_and( Prel >= min, Prel <= max)
    return Qads[b], Prel[b]


def linefit(x,y):
    """Does a least squares best line fit calculation to the x,y data
    passed in.  

    Returns a namedtouple with the following fields:  
    slope:                   Slope of best fit line. 
    y_intercept:             Y-Intercept of best fit line. 
    slope_err:               Uncertainty in the slope. 
    y_intercept_err:         Uncertainty in the intercept. 
    correlation_coefficient: Correlation coefficient (r) for the data. 
    """

    n = len(x)
    x2 = x*x

    D = np.sum(x2) - 1./n * sum(x)**2
    x_bar = np.mean(x)
    p, res, _, _, _ = np.polyfit(x, y, 1, full=True)

    slope = p[0]
    y_intercept = p[1]
    if n>2 :
        slope_err = math.sqrt(1./(n-2)*res/D)
        y_intercept_err = math.sqrt(1./(n-2)*(D/n + x_bar**2)*res/D)
    else:
        slope_err = 0
        y_intercept_err = 0
    correlation_coefficient = np.corrcoef(x, y)[0][1]

    return make_touple("LineFitData", 
        slope = slope,
        y_intercept = y_intercept,
        slope_err = slope_err,
        y_intercept_err = y_intercept_err,
        correlation_coefficient = correlation_coefficient, 
    )

