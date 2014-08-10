# These things are comments.  They dont get run as code
# and are just to explain whats happening

# Import os so we can clear screen
import os

# DEFINE FUNCTIONS - have to be defined above where you call them
def showMap():
    print "You have peaked at the secret map!"
    print "It shows you the choices from each room!"
    for t in transitions:
        print "Choices from " + t[0]
        for (i,c) in enumerate(transitions[t]):
            print i + 1, c[0]
    print ""
# STOP DEFINING FUNCTIONS

# These are Tuples (2 value pair)
# Think like a name and a value
# You get the first part with dungeon[0]
# and the second part with dungeon[1]
# COMPUTERS START NUMBERS WITH 0
# ZERO IS THE FIRST NUMBER
dungeon = ("Dungeon","You are in the dark dungeon of the castle\n" +
        "You find a strange hole in the wall")
tunnel = ("Tunnel","You are in a secret tunnel under the castle\n" +
        "You make your way to a ladder that leads to the Main Hall")
westHall = ("West Hall","You have entered the West Hall\n" +
        "This is the service area")
storeRoom = ("Storeroom","You have entered the storeroom\n" +
        "It is full of old barrels.")
pantry = ("Pantry","You have entered the pantry\n" +
        "FOOD! - Get one extra turn")
eastHall = ("East Hall","You have entered the East Hall...")
northHall = ("North Hall","You have entered the North Hall...")
southHall = ("South Hall","You have entered the South Hall...")
mainHall = ("Main Hall","You have entered the Main Hall...")
exitDoor = ("Strange Trap Door","You have found the secret exit!")

# This is a dictionary, it lets you map keys to values
# Here dungeon is the key and what is on the right of the :
# is the value it maps to.  Dictionaries let you look up 
# information by putting in the key
# Ex: transitons[dungeon] returns (westHall, eastHall) 
transitions = {
    dungeon: (tunnel,),
    tunnel: (mainHall,),
    westHall: (mainHall,pantry,storeRoom,),
    storeRoom: (westHall,),
    pantry: (westHall,),
    mainHall: (westHall,eastHall,northHall,southHall,),
    eastHall: (mainHall,exitDoor,),
    northHall: (mainHall,),
    southHall: (mainHall,)
}

# Lets start the game.  I'll put the player in the dungeon
location = dungeon
tries = 10
victory = False
print "WELCOME TO CHRISTINA'S CASTLE!"
print "YOU HAVE " + str(tries) + " TO ESCAPE!!!"

# While is a kind of loop... a control structure
# while True means loop over these lines forever
while tries > 0 and victory == False:
    os.system('clear')

    if map == True:
        showMap()
        map = False

    print location[1]
    print str(tries) + " turns remaining!"
    print "You can go to these places: "

    # for is another type of loop.  It says for each thing
    # in this output, do what is in the loop. 
    # Ex: transitions[location] will return where you
    #     can go.  enumerate returns the same output but
    #     also gives you a number.  So i is that number and t
    #     is the value. That print statement says:
    #     print i+1 (because 0 is the first number but humans
    #     dont like that. then also print the title of t after it.
    for (i,t) in enumerate(transitions[location]):
        print i + 1, t[0]

    # Last, we let them pick where to go next
    choice = raw_input("You choose: ")
    
    # SECRET CODE: if you type map it will print you a map
    if choice.lower() == "map":
        map = True
        continue
    else:
        try:
            choice = int(choice)
        # If they dont put in a number, dont count this turn
        # and handle the error and continue
        except (ValueError, TypeError):
            print "Only enter one of the listed numbers!"
            continue

    # and reset the location to what they chose
    try:
        location = transitions[location][choice - 1]
    # If the dictionary key isnt found, 
    # (they put in an invalid number)
    # then handle that error and dont count this turn
    except IndexError:
        print "Only enter one of the listed numbers!"
        continue
   
    # If they get to the exit, make them win
    if location[0] == exitDoor[0]:
        victory = True

    # Pantry doesn't deduct a turn
    if location[0] == pantry[0]:
        tries = tries + 2

    # Since it was a valid turn, take away one try
    tries = tries -1

if victory == True:
    print exitDoor[1]
    print "You have lived to escape the castle!"
else:
    print "You have died in the castle!"
