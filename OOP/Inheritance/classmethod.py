class Employee:
    company = "vuclip"
    salary = 100000
    location  = "pune"

#    def changeSalary(self, newsalary):
#        self.salary = newsalary             #changes salary of ofject/instance
#        self.__class__.salary = newsalary    #changes salary of class

             #or
    @classmethod
    def changeSalary(cls, newsalary):
        cls.salary = newsalary

        


e = Employee()
print(e.salary)
print(Employee.salary)

e.changeSalary(70000)
print(e.salary)
print(Employee.salary)
