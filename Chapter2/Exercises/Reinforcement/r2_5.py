from CreditCard import CreditCard

class CreditCardValidateNumber(CreditCard):
    
    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """

        try:
            price = float(price)
        except:
            raise ValueError("The price must be a number")

        if price + self.balance > self.limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""

        try:
            amount = float(amount)
        except:
            raise ValueError("The amount must be a number")

        self.balance -= amount