import unittest
from code_i_bank import *

import internet_bank_except

class NewTestInternetBank(unittest.TestCase):
    def setUp(self):
        self.terminal = InternetBank()
        self.terminal.enter_pin_code(333)

    def test_top_up_money(self):
        my_money = self.terminal.top_up_money(4000)
        self.assertEqual(my_money, 9000)

    def test_top_up_money_minus_odin(self):
        #Fail Test
        minus_odin = self.terminal.top_up_money(-1)
        self.assertEqual(minus_odin, "MinusOdin")

    def test_top_up_money_zero(self):
        #Fail Test
        zero = self.terminal.top_up_money(0)
        self.assertEqual(zero,"Zero")

    def test_top_money_plus_odin(self):
        plus_odin = self.terminal.top_up_money(1)
        self.assertEqual(plus_odin, 5001)

    def test_valid_pin_code(self):
        self.assertTrue(self.terminal.enter_pin_code(333))

    def test_correct_pin_code(self):
        self.terminal.enter_pin_code(333)
        self.assertTrue(self.terminal.user_can_get_money,True)

    def test_enter_pin_code_v2(self):
        self.terminal.enter_pin_code(333)
        self.assertEqual(self.terminal.attempts,3)

    def test_incorrect_enter_pin_code(self):
        self.terminal.enter_pin_code(222)
        self.assertEqual(self.terminal.attempts,2)


    def test_attempts(self):
        self.assertEqual(self.terminal.attempts,3)

    def test_incorrect_attempts(self):
        self.assertNotEqual(self.terminal.attempts,4)

    def test_incorrect_attempts_three(self):
        incorrect_attempts_1 = self.terminal.enter_pin_code(222)
        incorrect_attempts_2 = self.terminal.enter_pin_code(444)
        incorrect_attempts_3 = self.terminal.enter_pin_code(555)
        self.assertEqual(self.terminal.attempts, 0)
        self.assertTrue(self.terminal.user_can_get_money)

    def test_attempts_zero_return(self):
       #Kak npoBePuTb etot??
        self.terminal.enter_pin_code(885)
        self.terminal.enter_pin_code(232)
        self.terminal.enter_pin_code(123)
        self.terminal.enter_pin_code(333)
        self.assertTrue(self.terminal.user_can_get_money,)

    def test_snyat_dengi(self):
        self.terminal.snyat_dengi(4500)
        self.assertEqual(self.terminal.balance, 500)

    def test_snyat_dengi_granice_1(self):
        self.terminal.snyat_dengi(5000)
        self.assertEqual(self.terminal.balance,0)

    def test_snyat_dengi_granice_2(self):
        t = self.terminal.snyat_dengi(5001)
        self.assertEqual(t,"Error")

    def test_snyat_dengi_granice_3(self):
        self.terminal.snyat_dengi(1)
        self.assertEqual(self.terminal.balance,4999)

        #Kak Testit???
    def test_snyat_dengi_granice_4(self):
        self.terminal.snyat_dengi(0)
        self.assertEqual(self.terminal.balance,5000)
        # Kak Testit???
    def test_snyat_dengi_granice_5(self):
        self.terminal.snyat_dengi(-1)
        self.assertEqual(self.terminal.balance, 5000)

    def test_check_balance(self):
        self.terminal.enter_pin_code(333)
        self.terminal.check_balance()
        self.assertEqual(self.terminal.balance,5000)