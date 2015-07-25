from mic_report import bet, util, isotherm_examples as ex, plots
                    
s = ex.carbon_black()
min = 0.05
max = 0.3

plots.isoplot(s.Qads, s.Prel, s.descr[s.descr.find(':')+1:], min, max )

Q,P = util.restrict_isotherm(s.Qads, s.Prel, 0.05, 0.3)
B = bet.bet(Q, P, 0.162)
plots.betplot(P, B.transform, B.line_fit.slope, B.line_fit.y_intercept, max )

print("BET surface area: %.4f ± %.4f m²/g" % (B.sa, B.sa_err))
print("C:                %.6f" % B.C)
print("Qm:               %.4f cm³/g STP" % B.q_m)

