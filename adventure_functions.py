# These are the functions used by the adventure python program
# Written by Ethan Hendrickson; primarily for practicing the Python language

import time


# from adventure import player


# The following is the character class/object used for many in-game actions
class Character:

    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.x_position = 0
        self.y_position = 0

    def edit_inventory(self, thing):
        self.inventory.append(thing)


player = Character('Ethan')  # The player's character object


class Item:  # The class for item objects found in the game world

    def __init__(self, name):
        self.name = name
        self.x_position = 0
        self.y_position = 0


def intro():
    print("Welcome to Ethan's Adventure! Have fun, but be careful...")
    time.sleep(1)
    print("For a list of the available commands, type: what")
    time.sleep(1)
    location()


def what():
    print("Possible commands:")
    print("[what] - lists the possible commands")
    print("[whoami] - who am I")
    print("[look] - look around the room")
    print("[move (north/east/south/west)] - moves to the next room in the direction specified")
    print("[inventory] - lists the items in your inventory")
    print("[take] - begin placing an item in your inventory")
    return


def look():
    print("not coded yet")
    return


def move(user_input):
    print("not finished coding yet")

    if user_input == "move north":
        player.y_position += 1
    if user_input == "move east":
        player.x_position += 1
    if user_input == "move south":
        player.y_position -= 1
    if user_input == "move west":
        player.x_position -= 1

    #    print(player.x_position)
    #    print(player.y_position)
    location()
    return


def location():
    if int(player.x_position) == 0 and int(player.y_position) == 0:
        print("FRONT PORCH")
        print("You are standing in front of a one-story house. You can see: the front door, a mailbox, and two windows")

    if int(player.x_position) == -1 and int(player.y_position) == 1:
        print("DINING ROOM")
        print("You see: a large wooden table with a single wooden chair")
        print("Open doorways are on the eastern and northern walls.")

    if int(player.x_position) == 0 and int(player.y_position) == 1:
        print("FOYER")
        print("You see: a closed metal door (with a keypad) on the northern wall, and open doors to your east and west")

    if int(player.x_position) == 1 and int(player.y_position) == 1:
        print("OFFICE")
        print("You see: a colonial-style office with a large bookshelf.")
        print("The bookshelf is scarce, with only thirteen books filling its shelves.")
        print("Open doorways are on the western and northern walls")

    if int(player.x_position) == -1 and int(player.y_position) == 2:
        print("KITCHEN")
        print("You see: a contemporary kitchen; fully furnished with the classic kitchen appliances.")
        print("There is a single window above the sink.")
        print("Open doorways are on the southern and northern walls.")

    if int(player.x_position) == 0 and int(player.y_position) == 2:
        print("ELEVATOR")
        print("You see: a small, hotel-like elevator. There is a single button marked UP")
        print("UP")

    if int(player.x_position) == 1 and int(player.y_position) == 2:
        print("BATHROOM")
        print("You see: a full bathroom. Tile floors, bathtub/shower, sink, and toilet.")
        print("There is a pattern in the tiles shaped like an eight.")
        print("Open doorways are on the southern and northern walls.")

    if int(player.x_position) == -1 and int(player.y_position) == 3:
        print("KIDS BEDROOM")
        print("You see: a very scarce children's bedroom")
        print("Open doorways are on the eastern and southern walls.")
        print("There are two twin beds on the north/west walls.")

    if int(player.x_position) == 0 and int(player.y_position) == 3:
        print("BACK PORCH")
        print("You see: a wooden deck with doors leading to the east and west.")
        print("There is also a rope bridge that extends a bit to the north, leading to an interesting looking building")
        print("Three telescopes peer into the sky; each positioned to different positions")

    if int(player.x_position) == 1 and int(player.y_position) == 3:
        print("MASTER BEDROOM")
        print("You see: what looks to be a floor made of a bunch of king-sized beds pushed together.")
        print("You look at the beds and count. There are five beds in total.")
        print("This house is starting to seem strange. Fake in a way. Fabricated...")
        print("Open doorways are on the western and southern walls.")

    if int(player.x_position) == 0 and int(player.y_position) == 4:
        print("OBSERVATORY")
        print("You see: a fantastical laboratory.")




def take(item):
    print("unfinished")
    if item == 'knife':
        player.edit_inventory(item)
        print("You have picked up the " + item + ".")
    return


def inventory():
    print(*player.inventory, sep="\n")
    return

