class bank:
    def __init__(self,name,passwrd):
        self.name=name
        self.passwrd=passwrd
        self.balance=0
        print("Account Login")
        print("username:",self.name)
        print("password:",self.passwrd)
    def deposit(self,depositamnt):
        if depositamnt>0:
            self.balance+=depositamnt
            print("Amount deposit:",self.balance)
        else:
            print("Invalid deposit amount")
    def withdrawal(self,withdraw):
        if(self.balance>=withdraw):
            self.balance=self.balance-withdraw
            print("Amount withdrawal:",withdraw)
            print("Current balance:",self.balance)
        else:
            print("In sufficient balanace")



b=bank("Catherine","1234")
b.deposit(2000)
b.withdrawal(500)