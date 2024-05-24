print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#llamamos a la librería random para trabajar con ella
import random

#decimos que elija un número del 1 al 10 de manera aleatoria
number = random.randint(1,10)

#monitoreamos si el usuario adivinó el número
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That's correct!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))