from room import Room
from player import Player
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
player1 = Player("Fritz", "outside")
# Write a loop that:
# * Prints the current room name


def getRoom():
    return player1.current_room


# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def movePlayer(current):
    if current == "n":
        # if room[getRoom()].n_to != "":
        player1.set_current_room(room[str(player1.current_room).lower()].n_to)
    elif current == "s":
        player1.set_current_room(room[str(player1.current_room).lower()].s_to)
    elif whereTo == "e":
        player1.set_current_room(room[str(player1.current_room)].e_to)
    elif current == "w":
        player1.set_current_room(room[str(player1.current_room)].w_to)
    elif current == "q":
        print("Exited game!")
    else:
        print("Invalid entry")

# If the user enters a cardinal direction, attempt to move to the room there.


whereTo = ""

while whereTo is not "q":
    whereTo = input("Where do you want to go?:")
    print(getRoom())
    movePlayer(whereTo)
    print(getRoom())


# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
