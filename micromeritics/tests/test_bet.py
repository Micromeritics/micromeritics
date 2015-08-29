import numpy as np
import unittest
from micromeritics import bet

class TestBET(unittest.TestCase):
    def test_bet(self):
        Qads = np.array([4.67017, 4.79068, 4.9767, 5.14414, 5.31144, 5.47106,
                         5.63297, 5.80559, 5.96663, 6.13574, 6.31214, 6.49764,
                         6.67154])
        Prel = np.array([0.0672921, 0.0796994, 0.0999331, 0.119912, 0.140374,
                         0.159884, 0.179697, 0.200356, 0.219646, 0.239691,
                         0.259671, 0.280475, 0.299907])

        r = bet.bet(Qads, Prel, csa=0.162)
        np.testing.assert_almost_equal( r.sa, 20.7049, 4 )
        np.testing.assert_almost_equal( r.sa_err, 0.0289, 4 )
        np.testing.assert_almost_equal( r.C, 149.959660, 2 )
        np.testing.assert_almost_equal( r.q_m, 4.7569, 4 )

        roq = bet.Isotherm2RoquerolBET(Qads, Prel) 
        np.testing.assert_almost_equal( roq[0], 4.3559, 4 )
        np.testing.assert_almost_equal( roq[6], 4.62074, 4 )

if __name__ == '__main__':
    unittest.main()
