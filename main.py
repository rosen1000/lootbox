# TODO: add chroma support
# TODO: add daily rewards and such

import os
import json
import time
import progressbar
import pynotifier

from foundation import Foundation

if not os.path.exists("data"):
    os.mkdir("data")
if not os.path.exists("data/data.json"):
    with open("data/data.json", mode="x", encoding="utf-8") as file:
        file.write("{}")
        file.close()

game = None

SECOND = 1
MINUTE = SECOND * 60
HOUR = MINUTE * 60

def load():
    with open("data/data.json") as dataFile:
        global game
        game = json.load(dataFile)
def save():
    with open("data/data.json", "w") as dataFile:
        json.dump(game, dataFile)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def initGame():
    game["name"] = input("Enter your username: ")
    game["currency"] = {
        "blueEssence": 1000,
        "redEssence": 250,
        "blackEssence": 0
    }
    game["badLuckProtection"] = {
        "skinShard": 0,
        "gemstone": 0
    }
    game["inventory"] = {
        "champions": [],
        "skins": [],
        "chestNormal": 0
    }

def craftChest():
    print("Crafting a chest needs 10 minutes.\nProeed?")
    option = input("(y/n) > ")
    if option == "y":
        print("Please leave the program to craft your chest")
        print("Also resizing the window will break the progress bar :)")
        for i in progressbar.progressbar(range(1000)):
            time.sleep(MINUTE / 100)
        pynotifier.Notification(
            title="Chest has been crafted!",
            description="Come and claim your chest!"
        )
        print("Chest has been crafted! (Enter to claim)")
        input()
        game["inventory"]["chestNormal"] =+ 1

def openChest():
    # for i in progressbar.progressbar(range(10)):
    #     time.sleep(SECOND / 2)
    # TODO: openChest function
    pass

def openInventory():
    while True:
        clear()
        print("Blue essence: " + str(game["currency"]["blueEssence"]))
        print("Red essence: " + str(game["currency"]["redEssence"]))
        print("Black Essence: " + str(game["currency"]["blackEssence"]))
        print("Chests: " + str(game["inventory"]["chestNormal"]))
        print("Skins: " + str(len(game["inventory"]["skins"])))
        print()
        print("What do you want to do?")
        print("1. Unlock chests")
        print("2. Show Skins")
        print("0. Go back")
        option = input("> ")
        if option == "1":
            print("How many chests do you want to open?")
            toOpen = int(input("> "))
            if toOpen <= 0 or toOpen > game["inventory"]["chestNormal"]:
                print("Invalid number")
                continue
            for i in range(toOpen):
                openChest()
                input()
        elif option == "2":
            i = 0
            for skin in game["inventory"]["skins"]:
                print(skin)
                print("Do you want to do anything with them?")
                print("1. Enchant skin")
                print("2. Activate skin")
                print("3. Disenchant skin")
                print("0. Go back")
                option = input("> ")
                # TODO: operations on skins
                # NOTE: shard skins get blackEssence / 5 = redEssence
                # NOTE: perma skins get blackEssence / 2 = redEssence
                # NOTE: perma cost is rounded up
                if option == "1":
                    pass
                elif option == "2":
                    pass
                elif option == "3":
                    pass
                elif option == "0":
                    pass
                else:
                    pass
        elif option == "0":
            break
        else:
            print("Invalid option!")

def openShop():
    # TOOD: openShop function
    pass

load()
if game == {} or game == None:
    initGame()
    save()
# TODO: figlet title (pyfiglet)
while True:
    clear()
    print("What do you want to do?")
    print("1. Craft a chest")
    print("2. View inventory")
    print("3. Shop")
    print("4. Clear progress")
    print("0. Exit")
    option = input("> ")
    if option == "1":
        craftChest()
    elif option == "2":
        openInventory()
    elif option == "3":
        openShop()
    elif option == "4":
        print("WARNING! You are about to delete all of your progress")
        print("Please confirm your action by typing CONFIRM")
        if input("> ") == "CONFIRM":
            os.rmdir("data")
            print("Data removed")
            time.sleep(3)
            exit()
    elif option == "0":
        save()
        clear()
        exit()
