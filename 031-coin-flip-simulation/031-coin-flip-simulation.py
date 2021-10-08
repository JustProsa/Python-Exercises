# What's the minimum number of times you have to flip a coin before you can have three consecutive flips
# that result in the same outcome (either all three are heads or all three are tails)?
# What's the maximum number of flips that might be needed? How many flips are needed on average?
# In this exercise we will explore these questions by creating a program that simulates several series of coin flips.

# Create a program that uses a random number generator to simulate flipping a coin several times.
# The simulated coin should be fair, meaning that the probability of heads is equal to the probability of tails.
# Your program should flip simulated coins until either 3 consecutive heads of 3 consecutive tails occur.
# Display an H each time the outcome is heads, and a T each time the outcome is tails,
# with all of the outcomes for one simulation on the same line.
# Then display the number of flips that were needed to reach 3 consecutive occurrences of the same outcome.
# When your program is run it should perform the simulation 10 times and report the average number of flips needed.

import random


def head_or_tail():
    h_or_t = []
    while True:
        h_or_t.append(random.randint(0, 1))
        if h_or_t[len(h_or_t) - 1] == 1 and h_or_t[len(h_or_t) - 2] == 1 and h_or_t[len(h_or_t) - 3] == 1:
            break
    for num in h_or_t:
        if num == 0:
            print("H", end= " ")
        elif num == 1:
            print("T", end= " ")

    print("(" + str(len(h_or_t)) + " flips)")
head_or_tail()

