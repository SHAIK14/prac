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

    def __str__(self):
        return "hi this geneic trascaiton , so we do upi and bnefttandsacitosn "


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

    def __eq__(self, other):
        return self._amount == other._amount


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


t1 = UPITransaction("asif", "rishit", 10000, "asif@okaxis")
t2 = NEFTransaction("rahul", "rishit", 50000, "HDFC111")

print(t1 == t2)
