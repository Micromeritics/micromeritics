from micicromeritics import bet, util, isotherm_examples as ex, plots

#Setup the raw data for the calculation.  
s = ex.carbon_black()   # example isotherm of Carbon Black with N2.  
min = 0.05              # 0.05 to 0.30 range for BET 
max = 0.3
# Restrict the range of the isotherm to do the BET calcuation on.   
Q,P = util.restrict_isotherm(s.Qads, s.Prel, min, max)

# Show the full isotherm, and BET range.  
plots.isoplot(s.Qads, s.Prel, s.descr[s.descr.find(':')+1:], min, max )

# Do the BET calculation.  
B = bet.bet(Q, P, 0.162)

# Show the BET transform.  
plots.betplot(P, B.transform, B.line_fit.slope, B.line_fit.y_intercept, max )

# Show the results of the BET calculation.  
print("BET surface area: %.4f ± %.4f m²/g" % (B.sa, B.sa_err))
print("C:                %.6f" % B.C)
print("Qm:               %.4f cm³/g STP" % B.q_m)

