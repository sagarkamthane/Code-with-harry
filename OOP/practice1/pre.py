class Employee:

    salary = 11000
    increment = 1000

    @property
    def totalSalary(self):
        return self.salary + self.increment

    @totalSalary.setter
    def totalSalary(self, ts):
        self.increment = ts - self.salary




e = Employee()
print(e.totalSalary)

e.totalSalary = 14000
print(e.increment)
