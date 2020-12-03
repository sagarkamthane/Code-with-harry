with open('new.txt', 'r') as f:
    with open('new1.txt', 'w') as f1:
        f1.write(f.read())

with open('new1.txt', 'r') as f1:
    a = f1.read()
    print(a)

with open('new.txt', 'r') as f:
    with open('new1.txt', 'r') as f1:
        if f.read() == f1.read():
            print('same')

with open('new1.txt', 'w') as f1:
    f1.write('')