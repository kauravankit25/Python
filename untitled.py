from random import randint


def play(num):
    pguess =

    flag = True
    while flag:
        guess  = int(input("Guess the number:"))
        if guess == num:
            print("CONGRATULATIONS!!!\nYou have Won")
            break
        elif abs(guess - num) < abs(pguess - num):
            print("Warmer")
        elif abs(guess - num) > abs(pguess - num):
            print("Colder")
    ch = input("Guess again?(Y/N):")
    if ch.upper() == 'N':
        flag = False


# driver code
ch = True
while ch:
    n = randint(0, 100)

