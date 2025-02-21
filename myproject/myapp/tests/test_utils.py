# myapp/tests/test_utils.py
import unittest

from myproject.myapp.utils.my_utils import MyUtils


class MyUtilsTest(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(MyUtils.add_numbers(2, 3), 5)

    def test_multiply_numbers(self):
        self.assertEqual(MyUtils.multiply_numbers(2, 3), 6)
