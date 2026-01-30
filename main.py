from contextlib import nullcontext
import utilities
import character

import msvcrt
import sys

import threading
import keyboard
import pynput
from pynput.keyboard import Key, Controller

current_character = nullcontext

controller = Controller()

current_stat_update = character.Stats.NONE

def on_press(key):

    try:

        #print(f"{key.char}")
        if current_stat_update != character.Stats.NONE and (key.char == 'a' or key.char == 'd'):
            current_character.set_stat(current_stat_update, key.char)


    except AttributeError:
        pass

def start():
    global current_stat_update
    global current_character

    current_character = character.Character

    print("Enter character name.")

    current_character.set_name(input())

    print(f"Character named {current_character.name} has been created.")

    print("Set strength - a: subtract d: add")

    current_stat_update = character.Stats.Strength

    keyboard.wait("space")

    print("Set dexterity - a: subtract d: add")

    current_stat_update = character.Stats.Dexterity

    keyboard.wait("space")

    current_stat_update = character.Stats.NONE

    current_character.print_character_info()



def clear_keyboard_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()


# Start program
#start()
#utilities.testFile()

start()


clear_keyboard_buffer()

print("Buffer cleared. Program terminating.")
sys.exit()