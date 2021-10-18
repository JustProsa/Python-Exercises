# A magic date is a date where the day multiplied by the month is equal to the two digit year.
# For example, June 10, 1960 is a magic date because June is the sixth month,
# and 6 times 10 is 60, which is equal to the two digit year.
# Write a function that determines whether or not a date is a magic date.
# Use your function to create a main program that finds and displays all of the magic dates in the 20th century.

print("\nEnter the day")
day = int(input())
print("\nEnter the month")
month = int(input())
print("\nEnter the year")
year = int(input())

def magicDate(d, m, y):
    string_year = str(y)
    if d * m == int(string_year[len(string_year) - 2:]):
        print("\nYES! IT'S A MAGIC DATE!")
    else:
        print("\nNO! THAT'S NOT MAGIC!")

magicDate(day, month, year)






