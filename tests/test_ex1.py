import unittest
import sys, os

sys.path.append(os.getcwd())
from ex1 import *

class arithmetic_test(unittest.TestCase):
    def test_arithmetic_returns_answers(self):
        self.assertEqual(arithmetic(2, 3, "+"), 5)
        self.assertEqual(arithmetic(5, 3, "-"), 2)
        self.assertEqual(arithmetic(5, 4, "*"), 20)
        self.assertEqual(arithmetic(6, 3, "/"), 2)
        self.assertEqual(arithmetic(2, 3, ""), "Unknown operation")


if __name__ == '__main__':
    unittest.main()
