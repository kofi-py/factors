import unittest
from factors import find_factors


class TestFactors(unittest.TestCase):
    def test_basic(self):
        testcase = 24
        expected = [1, 2, 3, 4, 6, 8, 12, 24]
        self.assertEqual(find_factors(testcase), expected)
unittest.main()