class bank:
    def __init__(self,accno,name,type,balance):
        self.accno=accno
        self.name=name
        self.type=type
        self.balance=0
    def showact(self):
        print("Account holder name",self.name)
        print("Account number",self.accno)
        print("Account type",self.type)
        print("Your balance is",self.balance)
    def dep(self,d1):
        self.balance=self.balance+d1
        return self.balance
    def withd(self,w1):
        self.balance=self.balance-w1
        return self.balance
print("Enter the account details")
n=input("Enter your name")
a=int(input("Enter your account number"))
t=input("Enter your account type")
o=bank(n,a,t)
o.showact()
while(True):
    print("Menu \n 1.Deposit \n 2.Withdraw \n")
    choice=int(input("Enter your choice"))
    if(choice==1):
        amt=int(input("Enter the amount to be deposited \n"))
        o.dep(amt)
        o.showact()
    elif(choice==2):
        amt = int(input("Enter the amount to be withdrawed \n"))
        if(amt>o.balance):
            print("Insufficent balance \n")
        else:
            o.withd(amt)
            o.showact()
