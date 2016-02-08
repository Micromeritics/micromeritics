import numpy as np
from micromeritics import thickness as t
from micromeritics import plots

Prel = np.array([0.000000448802,0.000000936935,0.00000148652,0.00000209607,0.00000276863,0.00000351456,
                 0.00000435161,0.00000526938,0.00000630655,0.00000748296,0.00000884365,0.0000104439,0.0000123147,
                 0.0000146023,0.0000174301,0.0000209452,0.0000255346,0.0000314851,0.000039581,0.0000510105,
                 0.0000673633,0.0000921119,0.000132109,0.000203374,0.000346635,0.000670347,0.00109569,0.00127345,
                 0.00140321,0.00155907,0.00185297,0.00253435,0.00347369,0.00463502,0.00627777,0.00823441,0.0108343,
                 0.0308038,0.066713,0.0813908,0.100712,0.120399,0.14077,0.160733,0.180374,0.20067,0.250146,0.301205,
                 0.351224,0.400769,0.450922,0.50095,0.551038,0.601054,0.65121,0.701325,0.751307,0.801299,0.820996,
                 0.850996,0.875747,0.900984,0.925356,0.949191])

plots.plotThickness( Prel, t.KrukJaroniecSayari()(Prel), 'Kruk-Jaroniec-Sayari' )
plots.plotThickness( Prel, t.Halsey()(Prel), 'Halsey')
plots.plotThickness( Prel, t.HarkinsJura()(Prel), 'Harkins and Jura')
plots.plotThickness( Prel, t.BroekhoffDeBoer()(Prel), 'Broekhoff-de Boer')
plots.plotThickness( Prel, t.CarbonBlackSTSA()(Prel), 'Carbon Black STSA')
