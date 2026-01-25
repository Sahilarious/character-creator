import msvcrt
import sys


import threading
import keyboard
import pynput
from pynput.keyboard import Key, Controller
from enum import Enum

class Stats(Enum):
    NONE = 0
    Strength = 1
    Dexterity = 2
    Constitution = 3
    Intelligence = 4
    Wisdom = 5
    Charisma = 6

controller = Controller()

startingPointsPerStat = 8
maximumTotalPoints = 20 + 6 * startingPointsPerStat
currentPointsAvailable = maximumTotalPoints

maximumPointsPerStat = 20

characterName = ""
strength = startingPointsPerStat
dexterity = startingPointsPerStat
constitution = startingPointsPerStat
intelligence = startingPointsPerStat
wisdom = startingPointsPerStat
charisma = startingPointsPerStat

currentStatUpdate = Stats.NONE

def canAddPoints():
    if (strength + dexterity + constitution + intelligence + wisdom + charisma < maximumTotalPoints):
        return True
    else:
        return False
    
def printStats():
    print(f"Strength {strength}")
    print(f"Dexterity {dexterity}")
    print(f"Constitution {constitution}")
    print(f"Intelligence {intelligence}")
    print(f"Wisdom {wisdom}")
    print(f"Charisma {charisma}")

def onPress(key):

    try:

        #print(f"{key.char}")

        global strength
        global dexterity
        global constitution
        global intelligence
        global wisdom
        global charisma


        if currentStatUpdate != Stats.NONE and (key.char == 'a' or key.char == 'd'):
             if (currentStatUpdate == Stats.Strength):
                if key.char == 'a':
                    if strength > 1:
                        strength -= 1
                        print(f"{strength}")
                elif key.char == 'd':
                     if strength < maximumPointsPerStat:
                        strength += 1
                        print(f"{strength}")
             elif (currentStatUpdate == Stats.Dexterity):
                 if key.char == 'a':
                    if dexterity > 1:
                        dexterity -= 1
                        print(f"{dexterity}")
                 elif key.char == 'd':
                     if dexterity < maximumPointsPerStat:
                        dexterity += 1
                        print(f"{dexterity}")

             elif (currentStatUpdate == Stats.Constitution):
                    if key.char == 'a':
                        if constitution > 1:
                            constitution -= 1
                            print(f"{constitution}")
                    elif key.char == 'd':
                        if constitution < maximumPointsPerStat:
                            constitution += 1
                            print(f"{constitution}")

             elif (currentStatUpdate == Stats.Intelligence):
                  if key.char == 'a':
                        if intelligence > 1:
                            intelligence -= 1
                            print(f"{intelligence}")
                  elif key.char == 'd':
                     if intelligence < maximumPointsPerStat:
                        intelligence += 1
                        print(f"{intelligence}")

             elif (currentStatUpdate == Stats.Wisdom):
                    if key.char == 'a':
                        if wisdom > 1:
                            wisdom -= 1
                            print(f"{wisdom}")
                    elif key.char == 'd':
                         if wisdom < maximumPointsPerStat:
                             wisdom += 1
                             print(f"{wisdom}")
    
             elif (currentStatUpdate == Stats.Charisma):
                     if key.char == 'a':
                        if charisma > 1:
                            charisma -= 1
                            print(f"{charisma}")
                     elif key.char == 'd':
                        if charisma < maximumPointsPerStat:
                            charisma += 1
                            print(f"{charisma}")

    except AttributeError:
        pass


def updateStat(startValue):
    #selection = input()

    while(selection == 'a' or selection == 'd'):
        if selection == 'a':
            if startValue > 1:
                startValue -= 1
                print(f"{startValue}")
                #keyboard.wait('a')
        elif selection == 'd':
            if startValue < maximumPointsPerStat:
                startValue += 1
                print(f"{startValue}")
                #keyboard.wait('d')
        #selection = input()
        #keyboard.press(Key.enter)

    return startValue

def start():
    global strength
    global dexterity
    global currentStatUpdate

    print("Enter your character name")
    characterName = input()
    print(f"{characterName} has been created")
    printStats()

    print("Set strength - a: subtract d: add")

    print(f"Strength: {strength}")

    currentStatUpdate = Stats.Strength

    keyboard.wait("space")



    print("Set dexterity - a: subtract d: add")

    currentStatUpdate = Stats.Dexterity


    print(f"Dexterity: {dexterity}")

    keyboard.wait("space")


    #dexterity = updateStat(dexterity)

    printStats()

def clear_keyboard_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

#listeners
#with keyboard.Listener(on_press=onPress) as listener:
 #   listener.join() 

listener = pynput.keyboard.Listener(on_press=onPress)
listener.start()


# Start program
start()

clear_keyboard_buffer()

print("Buffer cleared. Program terminating.")
sys.exit()