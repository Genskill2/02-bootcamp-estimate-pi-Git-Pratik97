import math
import unittest
import random

def wallis(n):
        p_i = 1
        while (n > 0):
            p_i = p_i * (((4*n*n)/ ((4*n*n) - 1)))
            n -= 1
        return (2*p_i)
    
def monte_carlo(n_darts):
        in_region = 0
        n = n_darts
        while (n>0):
            x=random.random()
            y=random.random()

            s_dist=pow(x,2)+pow(y,2)
            dist=math.sqrt(s_dist)

            if (dist<1):
                in_region+=1
            n-=1

        pi_2=(4*(in_region)/(n_darts))

        return pi_2

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
