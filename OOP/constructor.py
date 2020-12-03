class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print("Employee is created")

    def getDetails(self):
        print(f"{self.name} is {self.age} years old and his salary is {self.salary} ")


sagar = Employee('sagar', 22, 15000)
sagar.getDetails()