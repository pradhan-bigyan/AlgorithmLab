import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        n = 9
        arr1 = list(range(1, n + 1)) 
        result1 = binary_search(arr1, 9)
        self.assertEqual(result1, 9)  
    
    def test_element_not_found(self):
        n = 9
        arr2 = list(range(1, n + 1)) 
        result2 = binary_search(arr2, 10)  
        self.assertEqual(result2, -1)  

if __name__ == '__main__':
    unittest.main()
