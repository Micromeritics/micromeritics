import numpy as np
import unittest
from micromeritics import util, isotherm_examples as ex

class TestUtil(unittest.TestCase):
    def test_restrict(self):
        s = ex.carbon_black()
        P,Q = util.restrict_isotherm( s.Prel, s.Qads, 0.05, 0.3 )
        self.assertTrue( Q.shape == P.shape )

        Qads = np.array([4.67017, 4.79068, 4.9767, 5.14414, 5.31144, 5.47106,
                         5.63297, 5.80559, 5.96663, 6.13574, 6.31214, 6.49764,
                         6.67154])
        Prel = np.array([0.0672921, 0.0796994, 0.0999331, 0.119912, 0.140374,
                         0.159884, 0.179697, 0.200356, 0.219646, 0.239691,
                         0.259671, 0.280475, 0.299907])
        self.assertTrue( (Qads == Q).all() )
        self.assertTrue( (Prel == P).all() )

if __name__ == '__main__':
    unittest.main()
