import unittest
from linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    def test_element_found(self):
        n = 100
        arr1 = list(range(1, n + 1))
        result1 = linear_search(arr1, n)
        self.assertEqual(result1, n)
    
    def test_element_not_found(self):
        n = 100
        arr2 = list(range(1, n + 1))
        result2 = linear_search(arr2, n+1)
        self.assertEqual(result2, -1)  

if __name__ == '__main__':
    unittest.main()
