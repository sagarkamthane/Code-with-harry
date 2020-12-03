no =int(input('enter a no: '))

prime = True
for i in range(2,no):
    if no%i==0:
        prime = False
        break

if prime:print(f"{no} is a prime no")
else:print(f"{no} is not a prime no")

