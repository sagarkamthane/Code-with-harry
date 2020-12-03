class Employee:
    company = 'Vuclip'

    def showDetails(self):
        print("this is employee")

class programmer(Employee):
    language = 'python'
    def getLang(self):
        print(f"Language:{self.language}")

    def showDetails(self):
        print("this is programmer")


e = Employee()
e.showDetails()

p = programmer()
p.showDetails()
print(p.company)
p.showDetails()
