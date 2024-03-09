import question_d

# Prompts user to enter their age
age = int(input("Please enter your age: "))

# This will check to see if the number entered is valid
while age < 0 or age > 125:
    age = int(input("The age entered is invalid. Please enter a valid age: "))

age_characterization = question_d.get_person_category(age)
print(age_characterization)