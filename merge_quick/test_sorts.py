import unittest
from mergesort import merge_sort
from quicksort import quick_sort

class TestSorts(unittest.TestCase):
    def test_merge_sort(self):
        input1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result1 = merge_sort(input1, 0, 8)
        self.assertListEqual(result1, expected1)
    
    def test_quick_sort(self):
        input2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result2 = quick_sort(input2, 0, 8)
        print(result2)
        self.assertListEqual(result2, expected2)

if __name__ == '__main__':
    unittest.main()