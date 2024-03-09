def get_random_number(guess, rand_num):
    while guess != rand_num:
        if guess < rand_num:
            return "The number guessed is larger. Try again."
        elif guess > rand_num:
            return "The number guess is smaller. Try again."
        elif guess == rand_num:
            return "You guessed the correct number!"