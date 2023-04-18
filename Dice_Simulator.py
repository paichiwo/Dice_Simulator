# Dice Simulator with API (random.org) and GUI

import random
import json
import requests
import PySimpleGUI as psg
import webbrowser

# Version
version = 'beta'

# Dictionary with dice images
dice_art_dict = {
    1: 'images/1.png',
    2: 'images/2.png',
    3: 'images/3.png',
    4: 'images/4.png',
    5: 'images/5.png',
    6: 'images/6.png',
    7: 'images/title.png',
    8: 'images/close.png'
}

# Customization
theme = psg.theme('black')
font = 'Young'


def create_window():
    # Function with application layout

    layout = [
        [psg.VPush()],
        [psg.Push(), psg.Image(dice_art_dict[8], pad=0,
                               enable_events=True,
                               key="-CLOSE-")],
        [psg.Text("GitHub",
                  font=f'{font} 10',
                  text_color="light green",
                  enable_events=True,
                  key="-LINK-"),
         psg.Push(),
         psg.Text(f'Version: {version}', font=f'{font} 10')],
        [psg.VPush()],
        [psg.Image(dice_art_dict[7], key="-OUTPUT-", size=(200, 200))],
        [psg.VPush()],
        [psg.Text("PRESS ROLL TO PLAY", font=f'{font} 10')],
        [psg.VPush()],
        [psg.Button("ROLL", key="-ROLL-",
                    border_width=0,
                    size=(5, 2),
                    button_color=('white', "red"),
                    font=f'{font} 16')],
        [psg.VPush()],
        [psg.Text("ROLLED NUMBERS:", font=f'{font} 10')],
        [psg.Text("", key="-ROLLED-", font=f'{font} 12')],
        [psg.VPush()],
        [psg.Text("AVERAGE:", font=f'{font} 10')],
        [psg.Text("", key="-AVG-", font=f'{font} 12')],
        [psg.VPush()]
    ]

    return psg.Window("Dice Simulator", layout,
                      size=(300, 520),
                      no_titlebar=True,
                      element_justification="center",
                      grab_anywhere=True,
                      finalize=True)


def roll_dice():
    # This function uses layout to create a window and contains all logic to roll the dice
    window = create_window()

    dice_list_str = []
    dice_list_int = []
    number_of_rolls = 0

    # Main loop
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, "-CLOSE-"):
            break

        # GitHub link event
        if event in "-LINK-":
            webbrowser.open("https://github.com/paichiwo")

        # Rolling dice
        if event == "-ROLL-":
            try:
                # Try rolling dice with API
                url = 'https://api.random.org/json-rpc/1/invoke'
                data = {'jsonrpc': '2.0',
                        'method': 'generateIntegers',
                        'params': {'apiKey': 'Your API key',        # YOUR KEY
                                   'n': 1, 'min': 1, 'max': 6,
                                   'base': 10}, 'id': 1}

                params = json.dumps(data)
                response = requests.post(url, params)
                json_dict = response.json()
                final = json_dict['result']['random']['data']
                dice = final[0]

            # If API fails use random module to roll the dice
            except requests.ConnectionError:
                dice = random.randint(1, 6)
            except requests.HTTPError:
                dice = random.randint(1, 6)
            except KeyError:
                dice = random.randint(1, 6)

            # Count number of rolls
            number_of_rolls += 1

            # Display rolled dice result image
            output_msg = dice_art_dict[dice]

            # Append result to list of strings and list of integers
            dice_list_str.append(str(dice))
            dice_list_int.append(dice)

            # Scroll if there are more than 18 results (>18 results will be longer than app width)
            if len(dice_list_str) > 18:
                del(dice_list_str[0])

            # Count sum of list with integers
            sum_of_rolls = sum(dice_list_int)

            # Convert list to sequence of numbers
            rolled_numbers = ", ".join(dice_list_str)

            # Display results
            window["-OUTPUT-"].update(output_msg, size=(200, 200))
            window["-ROLLED-"].update(rolled_numbers)
            window["-AVG-"].update(round(sum_of_rolls / number_of_rolls, 3))

    window.close()


if __name__ == '__main__':
    roll_dice()
