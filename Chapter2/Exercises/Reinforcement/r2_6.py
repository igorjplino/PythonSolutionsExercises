from CreditCard import CreditCard

class CreditCardWithPositiveAmount(CreditCard):
    
    def make_payment(self, amount):
        try:
            amount = float(amount)
        except:
            raise ValueError("The amount must be a number")

        if amount < 0:
            raise ValueError("The amount must be a positive number")

        self.balance -= amount