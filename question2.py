# Odd or Even Checker

# Write a Python program that asks the user for a number and then prints whether the number is
# odd or even.

# created a function called num_check that request a number input
def num_check():
 num = input("Enter a number: ")

# perform a check if the input provided is a number and convert the input to an integer
 if num.isdigit():
     num = int(num)

    #logic to check whether num satisfies the condition on being even or odd
     if num % 2 == 0:
        print("The number is even")
     else:
         print("The number odd")

# perform the magic check to see my output
num_check()






