# if with is used no need to close file

with open('new.txt', 'w') as f:
    f.write('I damn love python')

with open('new.txt', 'a') as f:
    f.write(',genuinly!')

with open('new.txt', 'r') as f:
    r = f.read()
    print(r)
