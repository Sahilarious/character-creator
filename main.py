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

def start():
    print("Enter your character name")
    characterName = input()
    print(f"{characterName} has been created")
    printStats()

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





start()