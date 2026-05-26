class UPITransaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.status = "pending"


paymentone = UPITransaction("asif", "rishit", 10000)
paymenttwo = UPITransaction("asif", "riverindie", 2500)
