import random

def game():
    newscore = random.randint(1,100)
    return newscore

a = str(game())


with open('game.txt', 'r') as f:
    s = f.read()
    if a>s:
        print(f'old:{s}, new:{a}')
        with open('game.txt', 'w') as f:
            f.write(a)
            print('score updated')
            if int(a)>70:
                f.truncate(0)
                print('file cleaned')

