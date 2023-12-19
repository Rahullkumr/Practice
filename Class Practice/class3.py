import datetime


class Age:
    def __init__(self):
        self.current_year = datetime.datetime.now().year


    def find_age(self,yob):
        self.year_of_birth=yob
        self.age = self.current_year - self.year_of_birth
        print(self.age)



year_of_birth = int(input("Enter birth year"))
a=Age()
a.find_age(year_of_birth)
