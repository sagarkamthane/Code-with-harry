m1 = int(input("Enter m1 marks"))
m2 = int(input("Enter m2 marks"))
m3 = int(input("Enter m3 marks"))

s  = (m1 + m2 + m3)/3
if (s > 40 ):
    if (m1>33 and m2>33 and m3>33):
        print("PASS", s)
else:print("Fail:", s)


