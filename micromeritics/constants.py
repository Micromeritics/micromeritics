"""This module defines physical constants that are used for the report models. 

In most cases this is a local wrapper for the scipy physical constants

VOLGASTP: Volume of one mole of gas at STP (cm^3)
AVOGADRO: Avegadro's number.  Number of molecules in a mole. 
NM2_M2:   Conversion factor from nm^2 to m^2. 
"""
import scipy.constants
import numpy

VOLGASTP  = pow(10,6) * scipy.constants.physical_constants['molar volume of ideal gas (273.15 K, 101.325 kPa)'][0]
AVOGADRO  = scipy.constants.N_A
NM2_M2    = 1.0E18
