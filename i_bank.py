import unittest
from code_i_bank import *

class TestInternetBank(unittest.TestCase):

    def setUp(self):
        self.terminal = InternetBank()
        self.terminal.enter_pin_code(333)

    def test_top_up_money(self):
        my_money = self.terminal.top_up_money(5000)
        self.assertEqual(my_money, 10000)

    def test_attempts(self):
        self.assertEqual(self.terminal.attempts, 3)

    def test_incorrect_attempts_(self):
        self.assertNotEqual(self.terminal.attempts, 4)

    def test_correct_pin_code(self,):
        self.terminal.enter_pin_code(333)
        self.assertTrue(self.terminal.user_can_get_money,True)

    def test_incorrect_pin_code_one(self):
        self.terminal.enter_pin_code(22)
        self.assertEqual(self.terminal.attempts, 2)

    def test_incorrect_pin_code_two(self):
        self.terminal.enter_pin_code(167)
        self.terminal.enter_pin_code(77)
        self.assertEqual(self.terminal.attempts, 1)

    def test_incorrect_pin_code_three(self):
        self.terminal.enter_pin_code(777)
        self.terminal.enter_pin_code(377)
        self.terminal.enter_pin_code(444)
        self.assertEqual(self.terminal.attempts, 0)

    def test_attempts_zero_return(self):
        self.terminal.enter_pin_code(555)
        self.terminal.enter_pin_code(609)
        self.terminal.enter_pin_code(000)
        self.terminal.enter_pin_code(333)
        self.assertEqual(self.terminal.enter_pin_code,"incorrect pin code")




