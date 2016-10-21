import unittest
from interpolate import interpolate

class TestInterpolate(unittest.TestCase):
    def test_flat(self):
        self.assertEqual(interpolate(1.,10., lambda x:4.,2.), 4.)

    def test_line(self):
        self.assertEqual(interpolate(1.,10., lambda x:1.+2.*x,2.), 5.)
        self.assertEqual(interpolate(10.,10., lambda x:1.+2.*x,10.), 21.)
