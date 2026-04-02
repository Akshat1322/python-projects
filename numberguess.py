import random

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

num = random.randint(low, high)

gc=0
ch=7

while gc < ch:
    gc += 1
    guess = int(input('your guess: '))

    if guess == num:
        print(f'your guess is right!!!! , you did it in {gc} chances')

    elif gc>=ch:
        print(f'sorry the number was {num} , you did not attemt in allowed chances')

    elif guess > num:
        print('too high , guess sth. small')

    elif guess<num:
        print('too small , guess sth. long')