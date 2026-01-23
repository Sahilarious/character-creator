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

def updateStat(startValue):
    selection = input()

    while(selection == 'a' or selection == 'd'):
        if selection == 'a':
            if startValue > 1:
                startValue -= 1
                print(f"{startValue}")
        elif selection == 'd':
            if startValue < maximumPointsPerStat:
                startValue += 1
                print(f"{startValue}")
        selection = input()

    return startValue

def start():
    global strength
    global dexterity
    print("Enter your character name")
    characterName = input()
    print(f"{characterName} has been created")
    printStats()

    print("Set strength - a: subtract d: add")

    print(f"Strength: {strength}")

    strength = updateStat(strength)

    print("Set dexterity - a: subtract d: add")

    print(f"Dexterity: {dexterity}")

    dexterity = updateStat(dexterity)

    printStats()




start()