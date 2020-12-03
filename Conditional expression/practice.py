a = int(input("enter a no"))
b = int(input("enter a no"))
c = int(input("enter a no"))
d = int(input("enter a no"))

# if (a>b) and (a>c) and (a>d):
#     print("a:", a)
# elif (b>a) and (b>c) and (b>d):
#         print("d:", b)
# elif(c>a) and (c>b) and (c>d):
#     print("c:", c)
# else:print("d:", d)

if (a>b):
    gr = a
else:
    gr = b

if (c>d):
    gr2 = c
else:
    gr2 = d

if (gr>gr2):
    print("Greatest no is:", gr)
else:print(gr2," is a greatest no")


