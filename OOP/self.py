class Employee:
    salary = "50000"
    def getSalary(self):
        print(f"salary : {self.salary}")

sagar = Employee()
print(sagar.salary)
sagar.getSalary()
sagar.salary = '60000'
Employee.getSalary(sagar)