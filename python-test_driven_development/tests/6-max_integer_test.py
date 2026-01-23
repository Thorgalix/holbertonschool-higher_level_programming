#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_all_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed(self):
        self.assertEqual(max_integer([-10, 0, 5, 2]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_max_at_start(self):
        self.assertEqual(max_integer([10, 1, 2]), 10)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 10, 2]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 10]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 2.0]), 2.5)


if __name__ == '__main__':
    unittest.main()
