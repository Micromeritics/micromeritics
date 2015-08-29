"""This module provides the t-Plot calculations on isotherm data.  
See: http://micro.edu/calculations/t-Plot.html for details. 
"""

import numpy as np
import math
import constants as const
import util

def tplot(Qads, Prel, thick_fcn,
          dcf, sacf, sa):
    """Run the t-Plot Calculation

    Arguments: 
    Qads: Quauntity of gas adsorbed (cm^3/g STP) (numpy array)
    Prel: Relative Pressure (numpy array)
    thick_fcn: The thickness function to use (thichness in A). 
    dcf: densift conversion factor (unitless)
    sacf: surface area correction factor (unitless)
    sa: surface area (m^2/g)

    Returns a namedtouple with the following fields:  
    t:          Thichness for the reltive pressures (A)
    ext_sq:     The t-Plot external surface area (m^2/g)
    ma:         The t-Plot micropore surface area (m^2/g)
    mv:         The t-Plot micropore volume (cm^3/g)

    """

    t = thick_fcn(Prel)
    lf = util.linefit(t, Qads)

    ext_sa = (lf.slope * dcf) / sacf * 10000
    ma = sa - ext_sa
    mv = lf.y_intercept * dcf
    
    return util.make_touple(
        "tPlotResults",
        t = t,
        ext_sa = ext_sa,
        mv = mv,
        ma = ma,
        line_fit=lf,
    )
