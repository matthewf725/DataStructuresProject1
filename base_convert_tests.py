import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        
    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    def test_base0(self):
        with self.assertRaises(ValueError):
            convert(10, 0)
    def test_base1(self):
        with self.assertRaises(ValueError):
            convert(10, 1)
    def test_belowZero(self):
        with self.assertRaises(ValueError):
            convert(-5, 4)
    
    def testLetter1(self):
        self.assertEqual(convert(290,14),"16A")
    def testLetter2(self):
        self.assertEqual(convert(291,14),"16B")    
    def testLetter3(self):
        self.assertEqual(convert(293,14),"16D")
    def testLetter4(self):
        self.assertEqual(convert(14,16),"E")
    def testLetter5(self):
        self.assertEqual(convert(15,16),"F")

if __name__ == "__main__":
        unittest.main()