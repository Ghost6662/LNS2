class BankAccount:
    def __init__(self, account_type, amount):
        self.account_type = account_type
        self.amount = amount
    def Deposit(self, Deposit_Amount):
        self.amount += Deposit_Amount
    def Withdraw (self, Withdraw_Amount):
        self.amount -= Withdraw_Amount
    def __str__(self):
        return "{} Account: {}".format(self.account_type, self.amount)
    def deleteAccount(self):
        self.amount = 0




Emil = BankAccount("Checkings", 100)
print(Emil)

Emil.Deposit(2000)

print (Emil)

Emil.Withdraw(300)

print (Emil)

Emil.deleteAccount()

print (Emil)