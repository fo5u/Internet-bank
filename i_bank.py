
import unittest
from internet_bank import *


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

    #def test_attempts_zero_return(self):
     #   self.terminal.enter_pin_code(555)
     #  self.terminal.enter_pin_code(609)
     #   self.terminal.enter_pin_code(000)
     #  self.terminal.enter_pin_code(333)
     #   self.assertEqual(self.terminal.enter_pin_code,"incorrect pin code")




    def test_correct_valid_pin_cod(self):
        self.assertTrue(self.terminal.enter_pin_code(333))

    def test_attempts_user_cat_return(self):
        incorrect_attemps_1 = self.terminal.enter_pin_code(555)
        incorrect_attempts_2 = self.terminal.enter_pin_code(609)
        incorrect_attempts_3 = self.terminal.enter_pin_code(000)
        self.assertEqual(self.terminal.attempts, 0)
        self.assertTrue(self.terminal.user_can_get_money)


    def test_balance_(self):
        minus_one = self.terminal.top_up_money(-1)
        self.assertEqual(minus_one, 5000)

    def test_balance_zero(self):
        #This test should be down
        plus_zero = self.terminal.top_up_money(0)
        self.assertEqual(plus_zero, 5000)

    def test_balance_one(self):
        plus_one = self.terminal.top_up_money(1)
        self.assertEqual(plus_one, 5001)

    def test_balance_text(self):
        vvod_text = self.terminal.top_up_money("love")
        self.assertEqual(vvod_text, 5000)

    def test_balance_text_plus_summa(self):
        vvod_text_sum = self.terminal.top_up_money("1dfhddf")
        self.assertEqual(vvod_text_sum, 5000)
