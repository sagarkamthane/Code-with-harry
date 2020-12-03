class Employee:
    def greet(self):
        print("Good morning")

    @staticmethod
    def wish():         #no need to pass self
        print("welcome!")

sagar = Employee()
sagar.greet()
sagar.wish()