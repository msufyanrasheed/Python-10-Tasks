class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance = self.balance - amount


acc = BankAccount("Ali", 1000)

acc.deposit(500)     
acc.withdraw(300)    
print(acc.balance)   

try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print("Error:", e)