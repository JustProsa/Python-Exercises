# Develop a program that reads a four-digit integer from the user and displays the sum of its digits. For example, if the user enters 3141 then your program should display 3+1+4+1=9.
print("\nEnter the 5-digits number")
number = int(input())
number = number * 10
print(number)
for n in range(int(number[0]), int(number[len(number) - 1])):
    print(n, end= ' + ')