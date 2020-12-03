class Person:

    def __init__(self):
        print("initializing person")
    country = 'India'

    def takeBreath(self):
        print("I'm Breathing")

    def place(self):
        print("I live on earth")

class Employee(Person):

    def __init__(self):
        super().__init__()
        print("initializing Employee")

    company = 'Honda'
    salary = "100k"
    def getSalary(self):
        print(f"salary: {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("Employee is breathing")

class Programmer(Employee):
    company = 'Kwid'

    def getSalary(self):
        super().getSalary()
        print(f"No salary for Programmer")




p = Programmer()

print(p.company)
p.getSalary()
p.takeBreath()
p.place()
print(p.country)
p.__init__()