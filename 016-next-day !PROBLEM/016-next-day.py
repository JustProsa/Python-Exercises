# Write a program that reads a date from the user and computes its immediate successor. For example, if the user enters values that represent 2019-11-18 then your program should display a message indicating that the day immediately after 2019-11-18 is 2019-11-19. If the user enters values that represent 2019-11-30 then the program should indicate that the next day is 2019-12-01. If the user enters values that represent 2019-12-31 then the program should indicate that the next day is 2020-01-01. The date will be entered in numeric form with three separate input statements; one for the year, one for the month, and one for the day. Ensure that your program works correctly for leap years.

print("\nEnter a day")
day = int(input())

print("\nEnter a month")
month = int(input())

print("\nEnter a year")
year = int(input())

def next_day():
    if day == 30 and month == 4 or month == 6 or month == 9 or month == 11:
        print("Next day is: " + "01" + " / " + "{:02d}".format(month + 1) + " / " + str(year))
    elif  day == 31 and month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        print("Next day is: " + "01" + " / " + "{:02d}".format(month + 1) + " / " + str(year))
    elif month == 12 and day == 31:
        print("Next day is: " + "01 / 01" + " / " + str(year + 1))
    elif month == 2 and day == 28 and year % 400 == 0:
        print("Next day is: " + str(day + 1) + " / " + str(month) + " / " + str(year))
    elif month == 2 and day == 28 and year % 100 == 0 and year % 400 != 0:
        print("Next day is: " + "01" + " / " + "{:02d}".format(month + 1) + " / " + str(year))
    elif month == 2 and day == 28 and year % 4 == 0 and year % 400 != 0 and year % 100 != 0:
        print("Next day is: " + str(day + 1) + " / " + "{:02d}".format(month) + " / " + str(year))
    elif day == 29 and month == 2 and year % 4 == 0:
        print("Next day is: " + "01" + " / " + "{:02d}".format(month + 1) + " / " + str(year))
    elif month == 2 and day == 28 and year % 4 != 0:
        print("Next day is: " + "01" + " / " + "{:02d}".format(month + 1) + " / " + str(year))

    else:
        print("Next day is: " + "{:02d}".format(day + 1) + " / " + "{:02d}".format(month) + " / " + str(year))

next_day()