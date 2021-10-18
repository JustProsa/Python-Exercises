# Positions on a chess board are identified by a letter and a number. The letter identifies the column, while the number identifies the row, as shown below: Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular arithmetic to report the color of the square in that row. For example, if the user enters a1 then your program should report that the square is black. If the user enters d5 then your program should report that the square is white. Your program may assume that a valid position will always be entered. It does not need to perform any error checking.

print("\nEnter the column of the board (a-h)")
column = input()
if column == "a" or column == "c" or column == "e" or column == "g":
    print("\nThe column " + column + " starts with a BLACK square")
else:
    print("\nThe column " + column + " starts with a WHITE square")

print("\nNow enter the row of the board (1-8)")
row = input()
if column == "a" or column == "c" or column == "e" or column == "g" and int(row) % 2 == 0:
    print ("\nThe square " + column + row + " is WHITE.")
elif column == "a" or column == "c" or column == "e" or column == "g" and int(row) % 2 != 0:
    print ("\nThe square " + column + row + " is BLACK.")
elif column == "b" or column == "d" or column == "f" or column == "h" and int(row) % 2 == 0:
    print ("\nThe square " + column + row + " is BLACK.")
elif column == "b" or column == "d" or column == "f" or column == "h" and int(row) % 2 != 0:
    print ("\nThe square " + column + row + " is WHITE.")