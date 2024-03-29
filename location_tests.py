import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    # Add more tests!
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("San Luis Obispo", 35.3, -120.7)
        loc4 = loc1
        self.assertFalse(loc1 == loc3)
        self.assertFalse(loc1 == loc2)
        self.assertTrue(loc1 == loc4)
        locations = [loc1, loc2]
        self.assertTrue(loc1 in locations)
        self.assertTrue(loc4 in locations)


if __name__ == "__main__":
        unittest.main()
