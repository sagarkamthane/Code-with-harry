n1 = int(input("enter no1"))
n2 = int(input("enter no2"))
n3 = int(input("enter no3"))

def greatest(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:return n3
    elif n2>n3:
        return n2
    else:return n3

print(greatest(n1,n2,n3))
