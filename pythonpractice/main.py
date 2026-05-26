class UPITransaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.__amount = amount
        self.status = "pending"

    def show_details(self):
        print(f"{self.sender} sent {self.__amount} to the {self.receiver}")

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount > 0:
            self.__amount = amount


paymentone = UPITransaction("asif", "rishit", 10000)
paymenttwo = UPITransaction("asif", "riverindie", 2500)
print(paymentone.get_amount())
print(paymentone.set_amount(1000))
print(paymentone.get_amount())
