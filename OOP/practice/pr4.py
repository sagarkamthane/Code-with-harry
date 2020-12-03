class calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def greet():
        print("Hello sagar!")

    def square(self):
        print(f'square of a no is {self.n ** 2}')

    def cube(self):
        print(f'cube of a no is {self.n ** 3}')

    def squretoot(self):
        print(f'square of a no is {self.n ** (1/2)}')


calc = calculator(9)
calc.greet()
calc.square()
calc.cube()
calc.squretoot()