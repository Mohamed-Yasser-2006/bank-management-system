class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Withdraw Successful")
        else:
            print("insufficient Balance")
    def transfer(self,outher_account,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            outher_account.deposit(amount)
            print("Transfer successful")
        else:
            print("Insufficient Balance")
accounts=[
    Bank("Mohamed",1000),
    Bank("Yasser",700)
]
while True:
    print("1-Show Account")
    print("2-Add Acount")
    print("3-Search Acount")
    print("4-Deposit")
    print("5-Withdraw")
    print("6-Transfer Money")
    print("7-Delete Account")
    print("8-Richest Account")
    print("9-Show Total Money In Bank")
    print("10-Show Account Count")
    print("11-Exit")
    choice=input("chose:")
    if choice=="1":
        for account in accounts:
            print(account.get_owner(),"-",account.get_balance())
        print("-"*20)
    elif choice=="2":
        owner=input("Enter Name:")
        balance=int(input("Balance:"))
        accounts.append(Bank(owner,balance))
        print("Added Successful")
        print("-"*20)
    elif choice=="3":
        search_name=input("Enter Name:")
        found=False
        for account in accounts:
            if account.get_owner()==search_name:
                print("Name Account",account.get_owner())
                print("Balance",account.get_balance())
                found=True
        if not found:
            print("Owner not Found")
        print("-"*20)
    elif choice=="4":
        found=False
        deposit_name=input("Enter Name:")
        deposit_amount=int(input("Amount:"))
        for account in accounts:
            if account.get_owner()==deposit_name:
                account.deposit(deposit_amount)
                print("New Balance:",account.get_balance())
                found=True
        if not found:
            print("Owner Not Found")
        print("-"*20)
    elif choice=="5":
        found=False
        withdraw_name=input("Enter Name:")
        withdraw_amount=int(input("Amount:"))
        for account in accounts:
            if account.get_owner()==withdraw_name:
                account.withdraw(withdraw_amount)
                print("New Balance:",account.get_balance())
                found=True
        if not found:
            print("Owner Not Found")
        print("-"*20)
    elif choice=="6":
        sender=None
        receiv=None
        sender_name=input("Enter Sender's Name:")
        receiver_name=input("Enter Receiver's Name:")
        amount=int(input("Enter Amount:"))
        for account in accounts:
            if account.get_owner()==sender_name:
                sender=account
            if account.get_owner()==receiver_name:
                receiv=account
        if sender and receiv:
            sender.transfer(receiv,amount)
        else:
            print("Owner Not Found")
        print("-"*20)
    elif choice=="7":
        found=False
        delete_name=input("Enter Name:")
        for account in accounts:
            if account.get_owner()==delete_name:
                accounts.remove(account)
                found=True
                break
        if not found:
            print("Owner Not Found")
        print('-'*20)
    elif choice=="8":
        richest_account=accounts[0]
        for account in accounts:
            if account.get_balance() > richest_account.get_balance():
                richest_account=account
        print("Richest Account:",richest_account.get_owner())
        print("Balance:",richest_account.get_balance())
        print("-"*20)
    elif choice=="9":
        total=0
        for account in accounts:
            total=total+account.get_balance()
        print("Total Money In Bank:",total)
        print("-"*20)   
    elif choice=="10":
        print("Account Count:",len(accounts))
        print("-"*20)
    elif choice=="11":
        print("Good Bye")
        break