import unittest

from main import *


class TestNumbers(unittest.TestCase):

    def test_integers(self):
        """
        this test asserts the sum of the numbers is of type integer
        """
        self.assertTrue(type(sumOfNumbers(6,6)) is int)
    
    def test_sum(self):
        """
        this test asserts the sum of the tested values equates to 3
        """
        self.assertEqual(sumOfNumbers(5,5), 10)




if __name__ == "__main__":
    unittest.main()