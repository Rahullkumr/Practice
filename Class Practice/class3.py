# write a python class that finds the age of a person.

import datetime
class Umar:
    def __init__(self):
        self.current_year = datetime.datetime.now().year        

    def display(self, yob):
        self.age = self.current_year - yob
        print(self.age)

birth_year = int(input("Enter birth year: "))
umar = Umar()
umar.display(birth_year)