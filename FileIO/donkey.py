
with open('donkey.txt', 'r+') as f:
    a = f.read()
    a = a.replace('donkey', '######')
    print(a)
with open('donkey.txt', 'w') as f:
    f.write(a)

