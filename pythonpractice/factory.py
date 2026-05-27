class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self._amount = amount
        self.status = "pending"

    def show_details(self):
        print(f"{self.sender} sent {self._amount} to the {self.receiver}")

    def process_payment(self):
        print(" this is the generic print")


class UPITransaction(Transaction):
    def __init__(self, sender, receiver, amount, upi_id):
        super().__init__(sender, receiver, amount)
        self.upi_id = upi_id

    def show_details(self):
        print(
            f"{self.sender} sent {self._amount} to the {self.receiver} through the {self.upi_id}"
        )

    def process_payment(self):
        print(" this is the upi print")


class NEFTransaction(Transaction):
    def __init__(self, sender, receiver, amount, ifsc_code):
        super().__init__(sender, receiver, amount)
        self.ifsc_code = ifsc_code

    def show_details(self):
        print(
            f"{self.sender} sent {self._amount} to the {self.receiver} through this  {self.ifsc_code} code"
        )

    def process_payment(self):
        print(" this is the NEFT print")


class TransactionFactory:
    @staticmethod
    def create(method, sender, receiver, amount, identifier):
        if method == "upi":
            t = UPITransaction(sender, receiver, amount, identifier)
            return t
        elif method == "neft":
            t = NEFTransaction(sender, receiver, amount, identifier)
            return t
        else:
            print(" the transactioin method is not availbel")


t1 = TransactionFactory.create("upi", "asif", "rishith", "10000", "abc@upiid")
t1.show_details()

t2 = TransactionFactory.create("neft", "asif", "rishith", "10000", "HDFC11000111")
t2.show_details()
