# A class customer contains following details: customer name, customer id, customer a/c no.
# Write a program that initializes the data members and displays it.

class Customer:
    def __init__(self, name1, cid, ac):
        self.c_name = name1
        self.c_id = cid
        self.c_acc = ac

    def display(self):
        print(f"Name: {self.c_name}, Id: {self.c_id}, Account: {self.c_acc}")

customer = Customer('Disha', '420', 'facebook')
customer.display()