import unittest

from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        self.assertEqual(max_list_iter([35, 41, 6, -1, 5]), 41)
        self.assertEqual(max_list_iter([2]), 2)
        self.assertEqual(max_list_iter([]), None)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([4]), [4])
        self.assertEqual(reverse_rec([]), [])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, low, high, list_val), 4)
        self.assertEqual(bin_search(5, low, high, list_val), None)  # target is not in list
        self.assertEqual(bin_search(2, 0, 0, [2]), 0)
        self.assertEqual(bin_search(0, 0, 0, []), None)

        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, None)


if __name__ == "__main__":
    unittest.main()
