# Welcome to the adventure
# This is a text-based adventure game similar to Zork
# It was programmed by Ethan Hendrickson; primarily for practicing the Python language

import adventure_functions

adventure_functions.intro()  # Prints the intro sequence

# creation_input = input("What is your name? ")
# print("Okay," + creation_input + "here we go.")
# player = adventure_functions.Character(creation_input)


while True:
    user_input = input("> ")
    if user_input == "what":
        adventure_functions.what()

    if user_input == "whoami":
        print("You are " + adventure_functions.player.name + " of course.")

    if user_input == "look":
        adventure_functions.look()

    if user_input == "move south" \
            or user_input == "move north" \
            or user_input == "move east" \
            or user_input == "move west":
        adventure_functions.move(user_input)

    if user_input == "take":
        item = input("What would you like to take: ")
        adventure_functions.take(item)

    if user_input == "inventory":
        adventure_functions.inventory()
