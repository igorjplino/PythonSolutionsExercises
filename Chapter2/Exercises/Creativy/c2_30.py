from CreditCard import CreditCard

class PredatoryCreditCard_c2_30(CreditCard):

    OVERLIMIT_FEE = 5
    
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self.apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            new_balance = self.balance + PredatoryCreditCard_c2_30.OVERLIMIT_FEE
            super()._set_balance(new_balance)
            
        return success

    def process_month(self):
        if self.balance > 0:
            monthly_factor = pow(1 + self.apr, 1/12)
            self.balance *= monthly_factor