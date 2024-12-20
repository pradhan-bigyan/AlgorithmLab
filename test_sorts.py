import unittest
from selectionsort import selection_sort
from insertionsort import insertion_sort

class TestSorts(unittest.TestCase):
    def test_selection_sort(self):
        input1 = [9,8,7,6,5,4,3,2,1]
        expected1 = [1,2,3,4,5,6,7,8,9]
        result1 = selection_sort(input1)
        self.assertListEqual(result1, expected1)
    
    def test_insertion_sort(self):
        input2 = [9,8,7,6,5,4,3,2,1]
        expected2 = [1,2,3,4,5,6,7,8,9]
        result2 = insertion_sort(input2)
        self.assertListEqual(result2, expected2)

if __name__ == '__main__':
    unittest.main()
