# Write two functions, hex2int and int2hex, that convert between hexadecimal digits
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and decimal (base 10) integers.
# The hex2int function is responsible for converting a string containing a single hexadecimal digit to a base 10 integer,
# while the int2hex function is responsible for converting an integer between 0 and 15 to a single hexadecimal digit.
# Each function will take the value to convert as its only parameter and return the converted value as its only result.
# Ensure that the hex2int function works correctly for both uppercase and lowercase letters.
# Your functions should display a meaningful error message and end the program if the parameter’s value is outside of the
# expected range.
import math
print("\nEnter your number (decimal or hexadecimal):")
number = input()

def int2hex(n):
    integers = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hexadecimals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    conversion = []
    while True:
        if int(n) / 16 > 0:
            q = math.floor(int(n) / 16)
            r = int(n) % 16
            conversion.insert(0, str(hexadecimals[r]))
            result = "".join(conversion)
            n = q
        else:
            conversion.insert(0, str(hexadecimals[n]))
            break
    return print(result)

def hex2int(n):
    integers = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hexadecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    conversion = []
    l = len(n) - 1
    p = 0
    while l >= 0:
        m = integers[hexadecimals.index(n[l])] * (16 ** p)
        conversion.append(int(m))
        l = l - 1
        p = p + 1

    result = sum(conversion)
    return print(result)


# if int(number) >= 0 and int(number) <= 99999999999999999999999999999999999999999999999:
#     int2hex(number)

hex2int(number)

