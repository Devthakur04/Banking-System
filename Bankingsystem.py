import random      
class BankAccount():
    def __init__(self):
        self.accounts={}

    def create(self,username):
        acc_no = random.randint(1000, 9999)
        while acc_no in self.accounts:
            acc_no = random.randint(1000, 9999)
        self.accounts[acc_no] = {'balance': 0, 'transactions': []}
        print(f"Account created successfully! Your account number is {acc_no}")
        return acc_no in self.accounts

    def login(self,acc_no):
        if acc_no in self.accounts:
            print("login successfully")
            return acc_no
        else:
            print("invalid account number")

    def logout(self):
        print("logout successfully")


class Operation():
    def __init__(self,acc_no):
        self.transactions=[]
        self.acc_no=acc_no
        self.balance=0


    def deposit(self,acc_no,amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self,acc_no,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def showtransaction(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def show_info(self,acc_no):
            print("account information")
            print(f"your account number is:{acc_no}")
            print(f"balance:{self.balance}")



def main():
    bank=BankAccount()
    operation=Operation(1234)
    while True:
        print("welcome to world bank")
        print("0: create account")
        print("1:login into account")
        print("2:exit")

        choice=int(input("enter your choice:"))

        if(choice==0):
            print("\nCreate account")
            username=input(("enter your name:"))
            bank.create(username)

        elif(choice==1):
            print("\nlogin into account")
            acc_no=int(input("enter your account number:"))
            session=bank.login(acc_no)
            while True:
                    print("0:show account information")
                    print("1:show transaction")
                    print("2:deposit")
                    print("3:withdraw")
                    print("4:logout")
                    
                    choice1=int(input("enter your choice1:"))
                    if(choice1==0):
                        print("\nshow account information")
                        c=int(input("enter your account number: "))
                        operation.show_info(acc_no)
                    elif(choice1==1):
                        print("\nshow transaction")
                        operation.showtransaction()
                    elif(choice1==2):
                        print("deposit")
                        amount=int(input("enter the amount you want to deposit:"))
                        operation.deposit(acc_no,amount)
                    elif(choice1==3):
                        print("withdraw")
                        amount=int(input("enter amount:"))
                        operation.withdraw(acc_no,amount)
                    elif(choice1==4):
                        print("logout ")
                        break
                    else:
                        print("invalid choice")
        
        elif(choice==2):
            print("exit!!\n")
            break
        else:
            print("invalid choice..")

main()




