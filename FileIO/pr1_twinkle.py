f = open('twinkle.txt', 'r')
a = f.read()
print(a.count('Twinkle')+ a.count('twinkle'))
f.close()



