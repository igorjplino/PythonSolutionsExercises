from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):

    OVERLIMIT_FEE = 5
    SURCHARGE = 1
    MAX_CHARGE = 10
    
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self.apr = apr
        self._amount_charge = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self.balance += PredatoryCreditCard.OVERLIMIT_FEE
        else:
            self._amount_charge += 1
        return success

    def process_month(self):
        if self.balance > 0:
            monthly_factor = pow(1 + self.apr, 1/12)
            self.balance *= monthly_factor
            if self._amount_charge > PredatoryCreditCard.MAX_CHARGE:
                self.balance += (self._amount_charge - PredatoryCreditCard.MAX_CHARGE) * PredatoryCreditCard.SURCHARGE
        self._amount_charge = 0