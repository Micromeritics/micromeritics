"""This module defines classes for thivhness curves
See: http://micro.edu/calculations/thickness.html for details. 
"""

import numpy as np
import math
from scipy import optimize

class  ThicknessCurve:
    """This provides the interface to all the thickness curves.  After
    construction, the object can be called like a function to evaluate
    the thickness for the relative pressure.
    """
    def eval(self, Prel):
        return 0

    def __call__(self, Prel):
        return self.eval(Prel)

class KrukJaroniecSayari(ThicknessCurve):
    """An instance of a ThicknessCurve that implements the Kruk-Jaroniec-Sayari model."""
    def __init__(self, c1 = 3.540, c2 = -5.000, c3 = 0.333):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def eval(self, Prel):
        return self.c1 * ((self.c2 / np.log(Prel))) ** self.c3

class Halsey(ThicknessCurve):
    """An instance of a ThicknessCurve that implements the Halsey model."""
    def __init__(self, c1 = 3.540, c2 = -5.000, c3 = 0.333):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def eval(self, Prel):
        return self.c1 * ((self.c2 / np.log(Prel))) ** self.c3

class HarkinsJura(ThicknessCurve):
    """An instance of a ThicknessCurve that implements the Harkins-Jura model."""
    def __init__(self, c1 = 13.9900, c2 = 0.0340, c3 = 0.500):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def eval(self, Prel):
        return (self.c1 / (self.c2 - np.log10(Prel))) ** self.c3

class BroekhoffDeBoer(ThicknessCurve):
    """An instance of a ThicknessCurve that implements the Broekhoff-de Boer model."""
    def __init__(self, c1 = -16.1100, c2 = 0.1682, c3 = -0.1137):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def eval(self, Prel):
        def f(x):
            return ( q - self.c2 * math.exp(self.c3 * x ) ) * (x ** 2) - self.c1
        xThickness = np.zeros(len(Prel))

        for i in range(0, len(Prel)):
            q = math.log10(Prel[i]) if (Prel[i] > 1E-10) else -10
            xThickness[i] = optimize.newton(f, 5.0, fprime = None, args = (), tol = 1.0e-6, maxiter = 50)
        return xThickness

class CarbonBlackSTSA(ThicknessCurve):
    """An instance of a ThicknessCurve that implements the Carbon Black STSA model."""
    def __init__(self, c1 = 2.9800, c2 = 6.4500, c3 = 0.8800):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def eval(self, Prel):
        return self.c1 + self.c2 * Prel + self.c3 * (Prel ** 2)
