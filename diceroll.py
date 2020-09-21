# Dice Roller for Warhammer and other multi-dice games
# Written by Andrew S-W to practice Python

import random

#Variables
rollarray = []
resetvalue = True

#Setup and While Loop
again = True
while again:
    quant = input("How Many Dice? ")
    sides = input("How Many Sides? ")
    rollover = input("How High do You Need to Roll? ")
#Dice Roll
    for i in range(int(quant)):
        rollarray.append(random.randint(1, int(sides)))
        overcount = sum(i >= int(rollover) for i in rollarray)
    print("Dice Results:", rollarray, "Successful Rolls:", int(overcount))
#Reset Dialogue
    another_roll = input('Roll again? ')
    if another_roll.lower() == 'yes' or another_roll.lower() == 'y':
        rollarray = []
        continue
    else:
        print("Thanks for Playing!")
        break