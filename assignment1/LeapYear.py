# This program checks if a given year is a leap year or not.
def is_leap(year):
    leap = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap



year = int(input("Enter a year: "))
print(is_leap(year))
