from micromeritics import langmuir, util, plots
from micromeritics import isotherm_examples as ex

# Setup the raw data for the calculation.  
# using example isotherm data from ZSM 5 with argon at 87K.
s = ex.zsm_5()   

# Do the Langmuir calculation. Then
# - show the transform plot
# - show the isotherm plot
# - print the Langmuir area, C constant, and monolayer quantity adsorbed
pmin = 0.0001
pmax = 1.0
csa_argon = 0.162
Lang_calc = langmuir.langmuir(s.Pabs, s.Qads, Pmin = pmin, Pmax = pmax, csa = csa_argon)
plots.plotLangmuirTransform(Lang_calc)
plots.plotLangmuirIsotherm(Lang_calc)
plots.addRangeBars(pmin, pmax)
plots.setXLog()
plots.show()
print("Langmuir surface area: %.4f m^2/g" % Lang_calc.sa)
print("Langmuir b: %.4f mmHg^-1" % Lang_calc.b)
print("Langmuir Qm: %.4f cm^3/g STP" % Lang_calc.qm)
