words = ['Donkey', 'donkey', 'Ass', 'jack', 'jenny', 'jennet', 'foal']

with open('donkey.txt', 'r') as f:
    a = f.read()
    for word in words:
        a = a.replace(word, '######')

with open('donkey.txt', 'w') as f:
    f.write(a)

with open('donkey.txt', 'r') as f:
    a = f.read()