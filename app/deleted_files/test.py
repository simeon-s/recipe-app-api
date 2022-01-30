from django.test import TestCase

# from app.calc import add
from calc import sum, subtract

# def sum(a,b):
#     return a+b

class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that 2 numbers are added together"""
        self.assertEqual(sum(3,8),11)

    def test_subtract_numbers(self):
        """ Test that values are subtracted and returned"""
        self.assertEqual(subtract(5,11),6)
