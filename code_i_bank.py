
import internet_bank_except

class InternetBank(object):
    balance = 5000
    attempts = 3
    user_can_get_money = False

    def top_up_money(self,my_money):
        if my_money == -1:
            raise ValueError
        else:
            return self.balance + my_money

    def enter_pin_code(self,pin_code):
        correct_pin_code = 333

        # if pin_code == str
        #     raise ValueError

        if self.attempts == 0:
            return "incorrect pin code"

        if pin_code != correct_pin_code:
            self.attempts = self.attempts - 1
            return "Error! Invalid pin code."

        if pin_code == correct_pin_code:
            self.user_can_get_money = True
            return True


    def snyat_dengi(self, minus_money):
        if self.user_can_get_money:

            if minus_money == -1:
                raise ValueError

            if minus_money <= self.balance:
                self.balance = self.balance - minus_money
                return minus_money
            else:
                return "Error"

    def confirm_the_balance(self, my_balance):
         if self.user_can_get_money:
            if my_balance == 1:
                return self.balance
            if my_balance!=1:
                return "No access"


