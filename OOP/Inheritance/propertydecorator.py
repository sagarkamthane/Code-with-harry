class Employee:
    company = 'Vuclip'
    salary = 5000
    bonus = 500

    @property
    def totalSal(self):
        return self.salary + self.bonus

    @totalSal.setter
    def totalSal(self, val):
        self.bonus = val - self.salary

e = Employee()
print(f'Total salary: {e.totalSal}')
e.totalSal = 6000
print(e.salary)
print(e.bonus)
