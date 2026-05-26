from abc import ABC, abstractmethod


class Transaction(ABC):
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self._amount = amount
        self.status = "pending"

    def show_details(self):
        print(f"{self.sender} sent {self._amount} to the {self.receiver}")

    @abstractmethod
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


transactions = [
    UPITransaction("asif", "rishith", "10000", "abc@upiid"),
    NEFTransaction("asif", "rishith", "10000", "HDFC11000111"),
]

for t in transactions:
    t.show_details()
    t.process_payment()
