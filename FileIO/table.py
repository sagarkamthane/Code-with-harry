for i in range(2, 21):
    for j in range(1,11):
        a = i* j
        with open(f'/Users/sagarkamthane/PycharmProjects/CODEWITHHARRY/tables/T{i}', 'a') as f:
            f.write(f'{str(a)}\n')
