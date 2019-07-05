import unittest
from internet_bank import *

class TestInternetBank(unittest.TestCase):

    def setUp(self):
        self.terminal = InternetBank()
        self.terminal.enter_pin_code(333)


    def test_top_up(self):
        my_money = self.terminal.top_up_money(5000)
        self.assertEqual(my_money, 10000)

    def test_attempts(self):
        self.assertEqual(self.terminal.attempts, 3)

    def test_attempts_minus(self):
        self.


