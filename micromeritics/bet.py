"""This module provides the BET calculations on isotherm data.  
See: http://micro.edu/calculations/bet.html for details. 
"""

import numpy as np
import math
from . import constants as const
from . import util

def Isotherm2BET(Qads, Prel) : 
    """Calculate the BET Transform

    Arguments: 
    Qads: Quauntity of gas adsorbed (cm^3/g STP) (numpy array)
    Prel: Relative Pressure (numpy array)

    Returns: BET transform of the data: 1/(Qads*(1/Prel-1))"""
    return 1/(Qads*(1/Prel-1))

def Isotherm2RoquerolBET(Qads, Prel) :
     """Calculate the Rouquerol BET Transform  Qads (1-Prel)

    Arguments: 
    Qads: Quauntity of gas adsorbed (cm^3/g STP) (numpy array)
    Prel: Relative Pressure (numpy array)

    Returns: BET Rouquerol transform of the data"""
     return Qads*(1-Prel)

def bet(Qads, Prel, csa):
    """Run the BET surface area calulation.  

    Arguments: 
    Qads: Quauntity of gas adsorbed (cm^3/g STP) (numpy array)
    Prel: Relative Pressure (numpy array)
    csa:  Molecular cross sectional area.  (nm^2)

    Returns a namedtouple with the following fields:  
    transform:  BET transform of the data: 1/(Qads*(1/Prel-1))
    C:          BET C value 
    sa:         BET Surface area (m^2/g)
    sa_err:     Uncertainty in the BET surface area. 
    q_m:        Monolayer capacity (cm^3/g STP)
    line_fit:   The line fit statistics from transform vs. Prel. 
    """

    transform = Isotherm2BET(Qads, Prel)
    lf = util.linefit(Prel, transform)

    C = (lf.slope + lf.y_intercept)/lf.y_intercept
    q_m = 1/(lf.slope + lf.y_intercept)
    sa = const.AVOGADRO*csa/(const.VOLGASTP*const.NM2_M2*(lf.slope + lf.y_intercept))
    sa_err = sa*(math.sqrt((lf.slope_err**2)+(lf.y_intercept_err**2))/(lf.slope+lf.y_intercept))
    
    return util.make_touple(
        "BETResults",
        transform = transform,
        C = C,
        q_m = q_m,
        sa = sa,
        sa_err = sa_err,
        line_fit=lf,
    )

def CalcBETArea(Qads, Prel, csa):
    """Calculates the BET Surface Area.  

    Arguments: 
    Qads: Quauntity of gas adsorbed (cm^3/g STP) (numpy array)
    Prel: Relative Pressure (numpy array)
    csa:  Molecular cross sectional area.  (nm^2)

    Returns: BET Surface area (m^2/g)
    """
    return bet(Qads, Prel, csa).sa

