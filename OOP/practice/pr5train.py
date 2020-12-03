class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Train Name : {self.name}")
        print(f"Seats Available : {self.seats}")

    def fareInfo(self):
        print(f"Ticket Price : {self.fare}")

    def Book(self):
        if self.seats > 0:
            print(f"Your seat no is: {self.seats} ")
            self.seats = self.seats - 1
        else:print("Sorry seat not available")

    def cancelticket(self):
        self.seats+=1
        print("Your ticket has been canceled")

Laturpune = Train('Latur-Pune', 450, 2)
Laturpune.getStatus()
Laturpune.fareInfo()
Laturpune.Book()
Laturpune.Book()
Laturpune.cancelticket()
Laturpune.Book()




