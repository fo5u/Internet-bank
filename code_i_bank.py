
from internet_bank_except import *

class InternetBank(object):
    balance = 5000
    attempts = 3
    user_can_get_money = False

    def top_up_money(self,my_money):
        if my_money == -1:
            raise MinusOdin

        if my_money == 0:
            raise Zero
        else:
            return self.balance + my_money

    def enter_pin_code(self,pin_code):
        correct_pin_code = 333

        if pin_code == str:
            raise String

        if self.attempts == 0:
            raise AttemtsOver

        if pin_code != correct_pin_code:
            self.attempts = self.attempts - 1
            #raise IncorrectPin

        if pin_code == correct_pin_code:
            self.user_can_get_money = True
            return True


    def snyat_dengi(self, minus_money):
        if self.user_can_get_money:

            if minus_money == -1:
                raise MinusOdin
            if minus_money == 0:
                raise Zero

            if minus_money == str:
                raise String

            if minus_money <= self.balance:
                self.balance = self.balance - minus_money
                return minus_money
            else:
                return "Error"

    def check_balance(self):
         if self.user_can_get_money:
            return self.balance
         else:
             raise EnterPin






