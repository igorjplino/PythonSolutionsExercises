from CreditCard import CreditCard

class CreditCardWithBalance(CreditCard):
    def __init__(self, customer, bank, acnt, limit, balance):
        super().__init__(customer, bank, acnt, limit, balance)