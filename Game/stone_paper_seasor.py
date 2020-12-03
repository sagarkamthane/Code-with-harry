import random

bot = random.randint(1, 3)
you = int(input('stone(1)?paper(2)?seasor(3)?'))
print(bot)

def game(comp, player):
    if comp == player : return None
    elif comp == 1:
        if player == 2: return True
        else: return False
    elif comp == 2:
        if player == 3: return True
        else: return False
    elif comp == 3:
        if player == 1: return True
        else: return False

a = game(bot, you)

if a == None : print('Tie')
elif a == True : print("You win")
else: print("You lose")
