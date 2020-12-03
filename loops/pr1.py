j = int(input('enter a no you wish to print table for'))

for i in range(1,11):
    print(str(j) + 'X' + str(i) + '=' + str(i*j))


for i in range(1,11):
    print(f"{j}X{i}={j*i}")   #fstring

i = 1
while i<11:
    print(f"{j}X{i}={j*i}")
    i=i+1