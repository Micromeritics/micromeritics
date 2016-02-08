from micromeritics import tplot, bet, thickness, util, plots
from micromeritics import isotherm_examples as ex

# Setup the raw data for the calculation.  
# using example isotherm data from Silica Alumina analyzed with N2.
s = ex.silica_alumina()

# Compute the BET surface area for this sample
# using the range 0.05 to 0.30, and the Cross-sectional area 
# for Nitrogen 0.162
BET_calc = bet.bet(s.Prel, s.Qads, Pmin = 0.05, Pmax = 0.3 , csa = 0.162)

# Do the tplot calculation.
TP_calc = tplot.tplot(s.Prel, s.Qads, thickness.HarkinsJura(), 
                      tmin = 3.0, tmax = 5.0, 
                      dcf = 0.0015468, sacf = 1.0, sa = BET_calc.sa )

plots.plotTPlot( TP_calc )
plots.show()

# Show the results of the tplot calculation.
print("Micropore Volume: %.4f cm^3/g" % TP_calc.mv)
print("Micropore Area: %.4f m^2/g" % TP_calc.ma)
print("External surface area: %.4f" % TP_calc.ext_sa)
print("Total surface area (BET): %.4f" % TP_calc.tot_sa)


