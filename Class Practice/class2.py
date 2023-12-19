class Customer:
    # name 
    # ac_no 
    # acc_type 
    # self.bal_amt 
    def __init__(self, name, ac_no, acc_type, amount):
        self.name = name
        self.ac_no = ac_no
        self.acc_type = acc_type
        self.amount = amount

    # deposit amt
    def deposit(self, deposit_amt):
        self.deposit_amt = deposit_amt
        self.amount += self.deposit_amt

    # withdraw after checking amt
    def withdraw(self, withdraw_amt):
        if self.amount < 100:
            print("Insufficient amount to withdraw")
        else:
            self.withdraw_amt = withdraw_amt
            self.amount -= self.withdraw_amt

    # display name and balance
    def display(self):
        print("Name: ", self.name)
        print("Balance: ", self.amount)


name = input("Enter your name: ")
acc_no = int(input("Enter your account number: "))
acc_type = input("Enter your account type (saving / current): ")

customer = Customer(name, acc_no, acc_type, 0)

deposit_amt = int(input("Enter amount to deposit: "))
customer.deposit(deposit_amt)
withdraw_amt = int(input("Enter amount to withdraw: "))
customer.withdraw(withdraw_amt)
customer.display()

