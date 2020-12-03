class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        return self.num + num2.num




n1 = Number(5)
n2 = Number(6)
print(n1 + n2)