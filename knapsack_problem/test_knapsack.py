from brute_force_01 import brute_force_01
from brute_force_frac import brute_force_frac
from greedy_frac import greedy_frac
from dynamic_01 import dynamic_01

import unittest

class TestKnapsack(unittest.TestCase):
    def test_01_brute(self):
        p = [60, 100, 120]
        w = [10, 20, 30]
        m = 50
        input = brute_force_01(p, w, m)
        output = 220
        
        self.assertEqual(input, output)
    
    def test_frac_brute(self):
        p = [60, 100, 120]
        w = [10, 20, 30]
        m = 50
        input = brute_force_frac(p, w, m)
        output = 240
        
        self.assertEqual(input, output)

    def test_frac_greedy(self):
        p = [60, 100, 120]
        w = [10, 20, 30]
        m = 50
        input = greedy_frac(p, w, m)
        output = 240
        
        self.assertEqual(input, output)
    
    def test_01_dynamic(self):
        p = [0,60, 100, 120]
        w = [0,10, 20, 30]
        m = 50
        n = 3
        input = dynamic_01(p, w, n,  m)
        output = 220
        
        self.assertEqual(input, output)
                
if __name__ == '__main__':
    unittest.main()