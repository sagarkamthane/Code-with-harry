class programmer:
    company = 'Vuclip'
    def __init__(self, name, profile, experience):
        self.name = name
        self.profile = profile
        self.experience = experience

    def progdetails(self):
        print(f'Name:{self.name}')
        print(f'Profile: {self.profile}')
        print(f'Experience: {self.experience}\n')

p1 = programmer('sagar', 'QA', 1)
p1.progdetails()

p2 = programmer('pranit', 'Automation QA', 1)
p2.progdetails()
