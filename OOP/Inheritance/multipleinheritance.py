class Employee:
    company = "google"
    code = 111

    def getInfo(self):
        print("This is employee")

class Freelancer:
    company = "Microsoft"
    level = 0

    def getInfo(self):
        print("This is Freelancer")

    def UpgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):      #properties of employee class has higher property
    name = 'sagar'


p = Programmer()
p.getInfo()
p.UpgradeLevel()

print(p.company)
