class Person:
    country = 'India'

    def takeBreath(self):
        print("I'm Breathing")

    def place(self):
        print("I live on earth")

class Employee(Person):
    company = 'Honda'

    def getSalary(self):
        print(f"salary: {self.salary}")

    def takeBreath(self):
        print("Employee is breathing")

class Programmer(Employee):
    company = 'Kwid'

    def getSalary(self):
        print(f"No salary for Programmer")


p = Programmer()

print(p.company)
p.getSalary()
p.takeBreath()
p.place()
print(p.country)