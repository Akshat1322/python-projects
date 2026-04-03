import random

name = input('Write your name: ')
print(f'Welcome {name}, Good Luck!')

words = ['drink', 'eat', 'sleep', 'code', 'play', 'read', 'write', 'run', 'jump', 'swim']
word = random.choice(words)

print('Guess the word, one character at a time!')

turns = 12
guesses = ''

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1

    print()

    if failed == 0:
        print(f' You won! The word was "{word}"')
        break

    guess = input('Make a guess: ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong guess!')
        print(f'You have {turns} turns left.')

        if turns == 0:
            print(f'You lost! The word was "{word}"')