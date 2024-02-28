import random

number = random.randint(1, 10)
while 1 == 1:
    guess = int(input())
    if number > guess:
        print("hoger")
    elif guess > number:
        print("lager")
    elif guess == number:
        print("win the corect number was " + str(number))
        break