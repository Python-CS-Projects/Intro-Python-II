from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Fritz", room["outside"])
# Write a loop that:
# * Prints the current room name


def getRoom():
    return player1.current_room

    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.


def movePlayer(current):

    if current == "n":
        if player1.current_room.n_to != None:
            player1.current_room = player1.current_room.n_to
        else:
            print("Wrong way, try again.")
    elif current == "s":
        if player1.current_room.s_to != None:
            player1.current_room = player1.current_room.s_to
        else:
            print("Wrong way, try again.")
    elif whereTo == "e":
        if player1.current_room.e_to != None:
            player1.current_room = player1.current_room.e_to
        else:
            print("Wrong way, try again.")
    elif current == "w":
        if player1.current_room.w_to != None:
            player1.current_room = player1.current_room.w_to
        else:
            print("Wrong way, try again.")
    elif current == "q":
        print("Exited game!")
    else:
        print("Invalid entry")

    # If the user enters a cardinal direction, attempt to move to the room there.


player1.current_room.set_items(Item("Test2", "test2"))
player1.current_room.set_items(Item("Test3", "test3"))


def get_item(item):
    for i in player1.current_room.items:
        if i.name == item:
            # remove item from room
            player1.current_room.on_take(i)
            # Add item to player items
            player1.set_item(i)
            return
        else:
            print("Item Not in this room")
            return


def drop_item(item):
    for i in player1.items:
        if i.name == item:
            # remove item from room
            player1.current_room.on_drop(i)
            # Add item to player items
            player1.remove_item(i)
            return
        else:
            print("Item dont below to player")
            return


whereTo = ""

while whereTo is not "q":
    print(getRoom())
    whereTo = input("Please enter a command:")
    if len(whereTo.split(" ")) == 1:
        movePlayer(whereTo)
        print(getRoom())
    else:
        action = whereTo.split(" ")[0]
        item = whereTo.split(" ")[1]
        if action == "take" or action == "get":
            get_item(item)
        elif action == "drop":
            drop_item(item)
        else:
            print("Invalid action")

            # Print an error message if the movement isn't allowed.
            #
            # If the user enters "q", quit the game.
