import random
playing = True
number=str(random.randint(10,20))

print("I will generate a number from 10 and 20 and you have to guess the number")
print("The game will end when you get it right")
while playing:
    guess=int(input(" Give me your best guess \n"))
    if number==guess:
        print("You win the game")
        print("The number was",number)
        break

    else:
        print("Your guess is not correct try again \n")