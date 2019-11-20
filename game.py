"""
Name: Legend of the Eclipse
Author: TimmiBowTie
"""

from map import map
import character

def intro():
    charName = ""
    charRace = ""
    charClass = ""

    print("Legend of the Eclipse")
    print()
    print("----")
    print("You try to open you eyes but they feel like they are weighed down by rocks.")
    print("You here a stirring around you and you attempt to grasp your weapon.")
    print("Before you know what is going on you hear a voice.")
    print("----")

    print("Strange voice:")
    print("Hello young traveler! What is your name?")

    charName = str(input())
    charName = charName.upper()

    print("Well {}, that is a good name for you! You do look".format(charName))
    print("a little funny! What is your race?")

    print()
    print("Select one of the below races by its number.")
    print("1.Elf \n2.Ork \n3.Human \n4.Dwarf \n5.Demon \n6.Angel ")

    charRace = str(input())

    if charRace == "1":
        charRace = "Elf"
    elif charRace == "2":
        charRace = "Ork"
    elif charRace == "3":
        charRace = "Human"
    elif charRace == "4":
        charRace = "Dwarf"
    elif charRace == "5":
        charRace = "Demon"
    elif charRace == "6":
        charRace = "Angel"
    else:
        print("You did not pick one of the given options. \nThe game will now close.")
        exit()

    if charRace == "Human":
        print("Ah yes, of course. The nose through me off \n, a little large ahaha.")
    else:
        print("We don't see many of you around here.")

    print()
    print("What type of warrior are you?")

    print()
    print("Select on of the below classes by its number.")
    print("1. Ranger \n2.Assassin \n3.Rogue \n4.Archane Knight \n5.Warrior \n6.Wizard")

    if charRace == "Elf":
        print("7.Elven Ranger")
    elif charRace == "Ork":
        print("7.Ork Battle Master")
    elif charRace == "Human":
        print("7.Templar")
    elif charRace == "Dwarf":
        print("7. Dwarven War Master")
    elif charRace == "Demon":
        print("7.Arch Angel")
    elif charRace == "Angel":
        print("7.Angelic Knight")

    charClass = str(input())

    if charClass == "1":
        charClass = "Ranger"
    elif charClass == "2":
        charClass = "Assassin"
    elif charClass == "3":
        charClass = "Rouge"
    elif charClass == "4":
        charClass = "Archane Knight"
    elif charClass == "5":
        charClass = "Warrior"
    elif charClass == "6":
        charClass = "Wizard"
    elif charClass == "7" and charRace == "Angel":
        charClass = "Angelic Knight"
    elif charClass == "7" and charRace == "Ork":
        charClass = "Ork Battle Master"
    elif charClass == "7" and charRace == "Human":
        charClass = "Templar"
    elif charClass == "7" and charRace == "Dwarf":
        charClass = "Dwarven War Master"
    elif charClass == "7" and charRace == "Demon":
        charClass = "Arch Angel"
    elif charClass == "7" and charRace == "Elf":
        charClass = "Elven Ranger"
    else:
        print("You did not pick one of the given options. \nThe game will now close.")
        exit()

    print()
    print("Wow well then you are quite the unique lad.")

    print("----")
    print("You feel a hand on your forehead and hear some inaudible whispers.")
    print("Suddenly light rush into your vision as you eyes lift.")
    print("You see yourself in an old, dimmley lit, wooden cabin.")
    print("As you sit up in the bed of furrs you see the old grizzled man sitting in front of you on a chair.")
    print("His half smile is awkward but he shows genuine worry for you.")

def run():
    pass

mapSet = map()

mapSet.move("Snowy Forest")


