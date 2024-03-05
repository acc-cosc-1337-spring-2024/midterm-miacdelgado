import question_b

# Prompts user for an int representing the day of the week
day = int(input("Please enter a number 1 - 7 representing the day of the week: "))

# This will check to see if the number entered is valid
while day < 1 or day > 7:
    day = int(input("The number entered is not valid. Please enter a number between 1-7: "))

# This will display what the day of the week is
day_result = question_b.get_day_of_week(day)
print(day_result)