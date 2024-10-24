# Grade Categorizer

# Write a program that takes a score (0-100) as input and categorizes it into one of the following
# grades:
# A (90-100)
# B (80-89)
# C (70-79)
# D (60-69)
# F (below 60)

def grade_categorizer():
    # request the user for score
    score = input("Enter score: ")

    # check if the score input is an integer
    if score.isdigit():
        score = int(score)

    if score >= 90:
        print("You have grade A")
    elif score >= 80:
        print("You have grade B")
    elif score >= 70:
         print("You have grade C")
    elif score >= 60:
         print("You have grade D")
    else:
        print("You have grade F")

# perform the function call
grade_categorizer()