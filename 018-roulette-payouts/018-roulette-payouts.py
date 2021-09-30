# A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two are green.
# The green spaces are numbered 0 and 00.
# The red spaces are numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36.
# The remaining integers between 1 and 36 are used to number the black spaces. Many different bets can be placed in roulette.

# We will only consider the following subset of them in this exercise:

# Single number (1 to 36, 0, or 00)
# Red versus Black
# Odd versus Even (Note that 0 and 00 do not pay out for even)
# 1 to 18 versus 19 to 36
# Write a program that simulates a spin of a roulette wheel by using a random number generator. Display the number that was selected and all of the bets that must be payed.

# For example, if 13 is selected then your program should display:

# The spin resulted in 13...
# Pay 13
# Pay Black
# Pay Odd
# Pay 1 to 18
# If the simulation results in 0 or 00 then your program should display Pay 0 or Pay 00 without any further output.

import random

# Starting conditions
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green_numbers = [00, 0]

print("\nLET'S START THE ROULETTE!")
print("\nWhat is your bet method?")
print("\nSingle number (1 to 36, 0, or 00)")
print("Red versus Black")
print("Odd versus Even (Note that 0 and 00 do not pay out for even)")
print("1 to 18 versus 19 to 36")
method_bet = input()

print("\nAnd now enter your bet!")
bet = input()

# Generate number
num = int(random.randint(00, 36))
print(num)



# Conditions
if num in red_numbers:
    single_number = "Pay red"
elif num in black_numbers:
    single_number = "Pay black"
elif num in green_numbers:
    single_number = "Pay green"

if num % 2 == 0:
    odd_or_even = "Pay Even"
else:
    odd_or_even = "Pay Even"

if num <= 18:
    range_number = "Pay 1 to 18"
else:
    range_number = "Pay 19 to 36"

# Results
print("Pay " + str(num))
print(single_number)
print(odd_or_even)
print(range_number)

