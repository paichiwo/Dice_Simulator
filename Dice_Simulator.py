# Dice simulator

import random as rnd

# Dictionary with dice images
dice_art_dict = {

    1: """
-------
|     |
|  o  |
|     |
-------
       """,
    2: """
-------
|     |
| o o |
|     |
-------
       """,
    3: """
-------
|   o |
|  o  |
| o   |
-------
       """,
    4: """
-------
| o o |
|     |
| o o |
-------
       """,
    5: """
-------
| o o |
|  o  |
| o o |
-------
       """,
    6: """
-------
| o o |
| o o |
| o o |
-------
       """
}
# Variables to count average
number_of_rolls = 0
sum_of_rolled_numbers = 0
rolled_numbers = []

# Main loop
while True:
    # asking user to start rolling dice or quit
    print('Press (p)lay roll a dice or (q)uit')
    choice = input()

    if choice == 'p':
        number_of_rolls = number_of_rolls + 1
        # dice roll
        dice = rnd.randint(1, 6)
        print(dice_art_dict[dice])
        rolled_numbers.append(dice)
    elif choice == 'w':
        sum_of_rolled_numbers = sum(rolled_numbers)
        print('Quitting')
        print(f'Average of rolled numbers: {round(sum_of_rolled_numbers / number_of_rolls)}')
        break
    elif choice != 'w' or choice != 'p':
        print('You didn\'t press (p) or (q)')
