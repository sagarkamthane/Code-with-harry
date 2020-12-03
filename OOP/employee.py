class Employee:
    company = "Google"
    salary = "10000"



harry = Employee()
sagar = Employee()
print(harry.company)
print(sagar.company)

Employee.company = 'Vuclip'
print(harry.company)
print(sagar.company)

print(sagar.salary)     #before creating object instance
sagar.salary = "15000"
print(sagar.salary)     # object instance has higher priority than class instance

print(sagar.address)    #throws error as no attribute named address present in class
