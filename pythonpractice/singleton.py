class DatabaseConnection:
    _instance = None

    def __new__(cls, connection_string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, connection_string):
        if not hasattr(self, "connection_string"):
            self.connection_string = connection_string

    def show_connection(self):
        print(self.connection_string)


db1 = DatabaseConnection("postgresql://localhost/payments")
db1.show_connection()

db2 = DatabaseConnection("postgresql://localhost/paymentssssssss")
db2.show_connection()

print(db1 is db2)
