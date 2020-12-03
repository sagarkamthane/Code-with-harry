for j in range(6):
    print(j)
else: print("else in for loop")

print('break') #exits for loop after 5
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("esle wont print as for loop has been breaked")

print('continue') #skips for loop for 5
for i in range(10):
    if i==5:
        continue
    print(i)