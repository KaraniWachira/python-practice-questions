# Simple Age Checker

# Write a Python program that asks the user for their age and tells them whether they are a minor
# (under 18), an adult (18-65), or a senior (over 65)


def age_checker():
    #request user for age input
    age = input("Enter your age: ")
    age = int(age)

    # logical condition to check whether is a minor and adult and senior
    if age < 18:
        print("You are a minor.")
    elif age <= 65:
        print("You are an adult.")
    else:
        print("You are a senior.")

# function call
age_checker()









