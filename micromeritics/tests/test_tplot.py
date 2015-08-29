import numpy as np
import unittest
from micromeritics import tplot
from micromeritics import thickness

class TestTPlot(unittest.TestCase):
    def test_tplot(self):
        
        Qads = np.array([116.296, 116.486, 116.634, 116.776,
                         116.895, 117.021, 117.126, 117.252, ])

        Prel = np.array([ 0.301205,   0.351224,   0.400769,   0.450922,   0.50095,
                          0.551038,   0.601054,  0.65121, ])

        Tcheck = np.array([5.02005, 5.35198, 5.69661, 6.06841,
                           6.46997, 6.91209, 7.40569, 7.96934, ])

        r = tplot.tplot( Qads, Prel, thickness.HarkinsJura(), 
                         dcf=0.0012800, sacf=1.000, sa=399.8633 )                      
        
        np.testing.assert_almost_equal( r.ext_sa, 4.0291, 3 )
        np.testing.assert_almost_equal( r.mv, 0.146955, 4 )
        np.testing.assert_almost_equal( r.ma, 395.8343, 2 )

        for i in range(len(Tcheck)) :
            np.testing.assert_almost_equal( Tcheck[i], r.t[i], 4 )

if __name__ == '__main__':
    unittest.main()

