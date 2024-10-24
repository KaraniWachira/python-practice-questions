# SIMPLE CALCULATOR

# Write a Python program that takes two numbers and
# an operation (+, -, *, /) from the user.
# Perform the operation and print the result.

def simple_calc():
   print("operator 1: Addition")
   print("operator 2: Subtraction")
   print("operator 3: Multiplication")
   print("operator 4: Division")

   # while loop to request the user to enter their operators choice
while True:
        operator = input("Enter operand (1, 2, 3, 4): ")

        if operator in ('1', '2', '3', '4'):
            operand1 = int(input("Enter first operand: "))
            operand2 = int(input("Enter second operand: "))

            if operator == '1':
                print(operand1, "+", operand2, "=", operand1 + operand2)

            elif operator == '2':
                print(operand1, "-", operand2, "=", operand1 - operand2)

            elif operator == '3':
                print(operand1, "*", operand2, "=", operand1 * operand2)

            elif operator == '4':
                print(operand1, "/", operand2, "=", operand1 / operand2)

            else:
                print("Invalid operator and operand")


            proceed = input("Do you want to proceed? (yes/no): ")
            if proceed.lower()!= 'yes':
                break

            print("Thank you!")


simple_calc()

































