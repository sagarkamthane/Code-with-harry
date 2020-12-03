class RailwayForm :
    formType = 'RailwayForm'
    def printData(self):
        print(f"Name: {self.name}")
        print(f"Train: {self.train}")

myForm = RailwayForm()
myForm.name = "Sagar"
myForm.train = "Bidar-Pune"
myForm.printData()


