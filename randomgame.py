#Number Guessing Game
#using random
from random import randint

num=randint(1,9)
num1=int(input("Enter the number you guessed: "))

if num==num1:
    print("Hurray! Guessed Correctly.")
elif num>num1:
    print("Oops! You guessed low.")
else:
    print("Oops! You guessed high.")
