import question_a
import random

rand_num = random.randrange(1,5)
print(rand_num)

print("Welcome to the random number guessing game.\n"
      "I've thought of a number between 1 and 5.\n"
      "And you have to guess it.")

guess = int(input("Please guess a number: "))

while guess < 1 or guess > 5:
    guess = int(input("The number entered is out of range. Please choose a number between 1 and 5: "))

while guess != rand_num:
    compare_guess = question_a.get_random_number(guess, rand_num)

    if guess > rand_num:
        print(compare_guess)
    elif guess < rand_num:
        print(compare_guess)
    elif guess == rand_num:
        print(compare_guess)
        break
    
    guess = int(input("Please guess a number: "))



