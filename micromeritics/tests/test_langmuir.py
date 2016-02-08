import numpy as np
import unittest
from micromeritics import util
from micromeritics import langmuir

class TestLangmuir(unittest.TestCase):
    def test_langmuir(self):

        # test with ZSM-5 (with argon) absolute pressure data
        Pabs = np.array([0.000550944, 0.00125234, 0.00201943, 0.00287494, 
                         0.00374617, 0.00472216, 0.00575706, 0.00685686, 
                         0.00804227, 0.00927519, 0.010638, 0.0120906, 
                         0.0136739, 0.0155067, 0.0175036, 0.0199029, 
                         0.0226501, 0.0265841, 0.0308749, 0.0360806, 
                         0.0429855, 0.0529933, 0.0670164, 0.089222, 
                         0.125268, 0.189935, 0.318431, 0.569838, 
                         0.815439, 1.46403, 2.376, 2.8266, 
                         3.61817, 4.48518, 5.04938, 5.87721, 
                         6.62262, 7.37314, 14.7118, 21.7727, 
                         33.4041, 42.4915, 59.7287, 77.0977, 
                         127.816, 164.812, 201.933, 238.912, 
                         275.867, 312.942, 350.292, 387.293, 
                         424.591, 461.675, 498.507, 535.264, 
                         573.143, 610.215, 647.152, 682.824, 713.608])

        Qads = np.array([2.9699, 5.93056, 8.88141, 11.8228, 
                         14.7718, 17.7248, 20.6808, 23.6441, 
                         26.5963, 29.5645, 32.5343, 35.4813, 
                         38.4156, 41.359, 44.3211, 47.3002, 
                         50.2784, 53.2155, 56.1965, 59.1842, 
                         62.1928, 65.2315, 68.1664, 71.143, 
                         74.037, 76.9003, 79.6843, 82.3116, 
                         84.9194, 97.9929, 102.401, 103.788, 
                         105.827, 107.372, 108.134, 109.077, 
                         109.779, 110.401, 114.195, 116.124, 
                         118.146, 119.254, 120.904, 122.263, 
                         125.676, 127.947, 130.109, 132.219, 
                         134.311, 136.4, 138.474, 140.467, 
                         142.502, 144.518, 146.572, 148.659, 
                         150.868, 153.107, 155.701, 159.725, 169.679])
        
        pmin = 10.0
        pmax = 150.0
        csa_argon = 0.162
        Lang_calc = langmuir.langmuir(Pabs, Qads, Pmin = pmin, Pmax = pmax, csa = csa_argon)
        np.testing.assert_almost_equal( Lang_calc.sa, 554.3504, 1 )
        np.testing.assert_almost_equal( Lang_calc.sa_err, 4.1514, 4 )
        np.testing.assert_almost_equal( Lang_calc.b, 0.401949, 4 )
        np.testing.assert_almost_equal( Lang_calc.qm, 127.3614, 2 )
        np.testing.assert_almost_equal( Lang_calc.transform_all[38], 0.12883, 5)
        np.testing.assert_almost_equal( Lang_calc.Qads_model[38] , 108.939, 2)


if __name__ == '__main__':
    unittest.main()
