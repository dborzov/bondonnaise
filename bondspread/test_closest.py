import unittest
from closest import closest

class TestClosest(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(closest([1,2,3], 2), 1)

    def test_both_sides(self):
        self.assertEqual(closest([1,2,3,4,5], 2.3), 1)
        self.assertEqual(closest([1,2,3,4,5], 2.8), 2)

    def test_outside_range(self):
        self.assertEqual(closest([1,2,3,4,5], 100), 4)
        self.assertEqual(closest([1,2,3,4,5], -100), 0)

    def test_one(self):
        self.assertEqual(closest([1], 2.3),0)
        self.assertEqual(closest([100], 2.3),0)
