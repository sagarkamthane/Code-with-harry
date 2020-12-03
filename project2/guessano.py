import random
with open('guesses.txt', 'w') as g:
    g.write('')
a = random.randint(1,100)
counts = []
guesses = []
guess = None
count = 0

while a!= guess or a == guess:
    guess = int(input("Guess: "))
    count += 1
    guesses.append(guess)
    counts.append(count)
    if guess<a:
        print("your guess is lower, enter a larger no")
    elif guess>a:
        print("your no is greater, enter a smaller no")
    else:
        print(f"your guess is correct: {a}, you took {count} attempts")
        break

with open('guesses.txt', 'r') as g
    read = None
    for Guesses
        read = g.readline()
    if guesses in
with open('guesses.txt', 'a') as g:
    g.write(f"Total guesses used: {count}\n")


