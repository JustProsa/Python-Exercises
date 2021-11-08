
bingo_card1 = {"B":[1, 7, 9, 4, 2],
               "I":[0, 0, 0, 0, 0],
               "N":[33, 42, 38, 32, 44],
               "G":[46, 60, 52, 57, 42],
               "O":[63, 64, 69, 72, 73]}

bingo_card2 = {"B":[0, 7, 9, 4, 2],
               "I":[0, 16, 24, 18, 29],
               "N":[0, 42, 38, 32, 44],
               "G":[0, 60, 52, 57, 42],
               "O":[0, 64, 69, 72, 73]}

bingo_card3 = {"B":[0, 7, 9, 4, 2],
               "I":[19, 0, 24, 18, 29],
               "N":[33, 42, 0, 32, 44],
               "G":[46, 60, 52, 0, 42],
               "O":[63, 64, 69, 72, 0]}

def winnerCard(card):
    print(card)
    list_numbers = list(card.values())
    diagonal = []
    vertical = []
    counter = 0
    counter1 = 0
    counter2 = 0
    while counter1 <= 4:
        diagonal.append(list_numbers[counter1][counter2])
        counter1 += 1
        counter2 += 1
    if sum(diagonal) == 0:
        return "Winner Card!"
    for val in list_numbers:
        if sum(val) == 0:
            return "Winner Card!"
        while counter <= 4:
            vertical.append(val[counter])
            counter += 1
    if sum(vertical[:5]) == 0 or sum(vertical[5:10]) == 0 or sum(vertical[10:15]) == 0 or sum(vertical[15:20]) == 0 or sum(vertical[20:25]) == 0:
        return "Winner Card!"
        
print(winnerCard(bingo_card1))
print("\n")
print(winnerCard(bingo_card2))
print("\n")
print(winnerCard(bingo_card3))
        
        