class programmer:
    def pDetails(self):
        print(f'Name:{self.name}')
        print(f'Designation: {self.deg}')


P1 = programmer()
P1.name = "sagar"
P1.deg = "QA"
P1.pDetails()

p2 = programmer()
p2.name = "neha"
p2.deg = "dev"
p2.pDetails()


