class Payment:
    def __init__(self, sender, amount, fee_stratergy):
        self.sender = sender
        self.amount = amount
        self.fee_stratergy = fee_stratergy

    def show_fee(self):
        return self.fee_stratergy.calculate(self.amount)


class Upistrat:
    def calculate(self, amount):
        return 0


class Neftstrat:
    def calculate(self, amount):
        return 2.5


upi = Payment("asif", 10000, Upistrat())
print(upi.show_fee())
neft = Payment("asif", 500, Neftstrat())
print(neft.show_fee())
