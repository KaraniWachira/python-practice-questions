# Day of the Week Checker
from pyqtgraph.examples.customPlot import dates


# Write a Python program that asks the user to enter a number (1 to 7) and prints the
# corresponding day of the week. If the number is outside the 1-7 range, print "Invalid input."

def week_checker():

    # dictionary to map the date integers to corresponding day of the week
    valid_dates = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    # request user for date input
    date = input("Enter a date ")

    if date.isdigit():
        date = int(date)

    # logic to check whether the input date matches the valid dates dictionary
    if date in valid_dates:
        print(valid_dates[date])
    else:
        print("Invalid input")


week_checker()

