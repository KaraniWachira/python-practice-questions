# Triangle Type Checker

# Write a Python program that takes the lengths of three sides of a triangle as input and
# determines if the triangle is:

# Equilateral (all sides are equal),
# Isosceles (two sides are equal), or
# Scalene (all sides are different).


def triangle_type_checker():

    length1 = input("Enter length1: ")
    length2 = input("Enter length2: ")
    length3 = input("Enter length3: ")

    if length1.isdigit() & length2.isdigit() & length3.isdigit():
        length1 = int(length1)
        length2 = int(length2)
        length3 = int(length3)

    if length1 == length2 == length3:
        print("This is an Equilateral Triangle")

    elif length1 == length2 or length1 == length3 or length2 == length3:
        print("This is an Isosceles Triangle")

    elif length1 != length3 or length2 != length1 or length3 != length2:
        print("This is a Scalene Triangle")

    else:
        print("invalid")


triangle_type_checker()



















