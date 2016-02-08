from micromeritics import bet, util, plots
from micromeritics import isotherm_examples as ex

# Setup the raw data for the calculation.  
# using example isotherm data from Carbon Black analyzed with N2.
s = ex.carbon_black()   

# Do the BET calculation. Then
# - show the transform plot
# - show the isotherm plot
# - print the BET area, C constant, and monolayer quantity adsorbed
BET_calc = bet.bet(s.Prel, s.Qads, Pmin = 0.05, Pmax = 0.3, csa = 0.162)
plots.plotBETTransform(BET_calc)
plots.plotBETIsotherm(BET_calc)
plots.addRangeBars(0.05, 0.3)
plots.show()
print("BET surface area: %.4f cm^3/g STP" % BET_calc.sa)
print("BET C: %.4f" % BET_calc.C)
print("BET Qm: %.4f cm^3/g STP" % BET_calc.q_m)
