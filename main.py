
""" Guess the number """

import math
import random

print("")
print("\t\tWELCOME TO GUESS THE NUMBER !!!!")

# TAKE THE LOWER LIMIT

lower_limit = int(input("\nEnter the LOWER LIMIT - "))

# TAKE THE UPPER LIMIT

upper_limit = int(input("\nEnter the UPPER LIMIT - "))

# Initialize a random number which user has to guess

number = random.randint(lower_limit, upper_limit)

# To decide number of chances to be given to the user to guess

X = round(math.log(upper_limit - lower_limit + 1, 2))
print("\n YOU HAVE ", X, "CHANCES")
count = 0

while(count<X):
    count+=1
    guess = int(input("\t\nGUESS THE NUMBER (CHANCE " + str(count) + ") - "))
    if(guess==number):
        print("\n\t\t CONGRATULATIONS!!!!!! \n\t\t YOU GUESSED IT RIGHT IN ", count, " TURNS")
        exit()
    elif(guess<number):
         print("\n YOU GUESSED TOO SMALL")
    else:
        print("\nYOU GUESSED TOO LARGE")

print("\n\t\t YOU LOST \t\n THE CORRECT NUMBER WAS ", number, "\n   BETTER LUCK NEXT TIME!")





