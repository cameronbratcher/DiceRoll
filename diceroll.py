#!/usr/bin/env python3

#Cameron Bratcher 2015
#Dice Rolling Simulator

import random

print("Dice Rolling Simulator\n")

die1 = random.randint(1,6)
die2 = random.randint(1,6)

#Dictionary for die options
dieOptions={
1:"-----\n|   |\n| o |\n|   |\n-----",
2:"-----\n|o  |\n|   |\n|  o|\n-----",
3:"-----\n|o  |\n| o |\n|  o|\n-----",
4:"-----\n|o o|\n|   |\n|o o|\n-----",
5:"-----\n|o o|\n| o |\n|o o|\n-----",
6:"-----\n|o o|\n|o o|\n|o o|\n-----"
}

print(dieOptions[die1])
print(dieOptions[die2])
