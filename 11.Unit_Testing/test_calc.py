import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)



"""
TODO: 

https://www.youtube.com/watch?v=6tNS--WetLI&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=21&pp=iAQB
"""