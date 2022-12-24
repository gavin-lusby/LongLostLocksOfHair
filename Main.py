# Author: Gavin Lusby
# Date: June 2020
# Description: Tkinter-based adventure game where main tries to regrow his lost hair


import os
import sys
import time
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()

def resource_path(relative_path):

    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)
# import Events

icon = resource_path("icon.ico")

def setupImage(
        imageName):  # Makes assigning images with a specific spec easier. Not in ease of access section cause that would cause "variable before assignment" errors
    imageName = "Images/" + imageName
    return ImageTk.PhotoImage(((Image.open(resource_path(imageName))).resize((800, 504), Image.NEAREST)).convert("RGBA"))


root.title("The Long Lost Locks(of hair)")
root.geometry("1280x720")
root.resizable(False, False)
root.iconbitmap(icon)

eventLabel = Label(root, width=166, borderwidth=60, bg="black", fg="white", relief=GROOVE, height=5, anchor=CENTER)
eventLabel.place(x=0, y=0)

# ---------------------------
# -----IMAGE DECLARATION-----
# ---------------------------




bgimage = ImageTk.PhotoImage(Image.open(resource_path("Images/homescreenbg.png")))  # pyimage1
brickwall = ImageTk.PhotoImage(Image.open(resource_path("Images/brickwall.png")))  # pyimage2
plantationImage = setupImage("plantation.png")  # pyimage3
plantationcloseImage = setupImage("plantationclose.png")  # pyimage4
fieldImage = setupImage("fields.png")  # pyimage5
village1Image = setupImage("villagescene1.png")  # pyimage6
baldentranceImage = setupImage("baldentrance.png")  # pyimage7
baldbasementImage = setupImage("baldbasement.png")  # pyimage8
compassN = ImageTk.PhotoImage(
    ((Image.open(resource_path("Images/compnor.png"))).resize((128, 128), Image.NEAREST)))  # pyimage9 (KEEP ORDER)
compassE = ImageTk.PhotoImage(
    ((Image.open(resource_path("Images/compeas.png"))).resize((128, 128), Image.NEAREST)))  # pyimage10(KEEP ORDER)
compassS = ImageTk.PhotoImage(
    ((Image.open(resource_path("Images/compsou.png"))).resize((128, 128), Image.NEAREST)))  # pyimage11(KEEP ORDER)
compassW = ImageTk.PhotoImage(
    ((Image.open(resource_path("Images/compwes.png"))).resize((128, 128), Image.NEAREST)))  # pyimage12(KEEP ORDER)

# Alphabetically ordered from now on
angrymanImage = setupImage("angryman.png")
arrestedImage = setupImage("arrested.png")
backyardImage = setupImage("backyard.png")
backyardHoleImage = setupImage("backyardhole.png")
basementImage = setupImage("basement.png")
bluedoorImage = setupImage("bluedoor.png")
blueopenImage = setupImage("bluedooropen.png")
bluekeyImage = setupImage("bluekey.png")
bunkerImage = setupImage("bunker.png")
bunkerOpenImage = setupImage("bunkerlucas.png")
greenkeyImage = setupImage("bunkerlucaskey.png")
deadyardImage = setupImage("deadowner.png")
dojoExtImage = setupImage("dojoouter.png")
dragonFightImage = setupImage("dragonfight.png")
farmHouseEntranceImage = setupImage("farmhouseentrance.png")
greendoorImage = setupImage("greendoor.png")
greenopenImage = setupImage("greendooropen.png")
dojoIntImage = setupImage("insidedojo.png")
leavingSwampImage = setupImage("junkmonk.png")
libraryImage = setupImage("library.png")
livingroomImage = setupImage("livingroom.png")
bigLossImage = setupImage("lose.png")
monkeyEatImage = setupImage("monkeyeat.png")
noShovelImage = setupImage("noshovel.png")
cellarImage = setupImage("orangecellar.png")
reddoorImage = setupImage("reddoor.png")
redopenImage = setupImage("reddooropen.png")
safeImage = setupImage("safe.png")
safeOpenImage = setupImage("safeopen.png")
safeRoomImage = setupImage("saferoom.png")
junkpileImage = setupImage("shoveljunk.png")
curiousGeorgeImage = setupImage("speakyellowmonk.png")
redkeyImage = setupImage("speakyellowkey.png")
swampImage = setupImage("swamp.png")
upstairsImage = setupImage("upstairs.png")
village2Image = setupImage("villagescene2.png")
village3Image = setupImage("villagescene3.png")
winImage = setupImage("win.png")


def printMessage(message, premessage):  # Prints message one char at a time, premessage = message already there
    global eventLabel
    current = premessage
    for letter in message:
        current = current + letter
        eventLabel.config(text=current)
        time.sleep(0.025)
        root.update()


# |||| same as printMessage but with extra params, p1,p2 etc = character to pause at
# VVVV p1l,p2l etc = pause length
def printMessagePause(message, premessage, p1, p2, p3, p4, p1l, p2l, p3l,
                      p4l):
    global eventLabel
    current = premessage
    counter = 0
    for letter in message:

        current = current + letter
        eventLabel.config(text=current)
        time.sleep(0.025)
        if p1 == counter:
            time.sleep(p1l)
        if p2 == counter:
            time.sleep(p2l)
        if p3 == counter:
            time.sleep(p3l)
        if p4 == counter:
            time.sleep(p4l)
        counter += 1
        root.update()


def submitName():  # What happens when player clicks submit name button, which sets the name if it is vaild, and if not, tells the user it is invald
    global b1
    print(b1)
    global name
    name = enterName.get()
    if name != "":
        enterName.place_forget()
        enterNameB.place_forget()
        startGame.phase2()
        root.unbind("<Return>", b1)
    else:
        root.unbind("<Return>", b1)  # Lambda binded here then unbinded on 74 so user cant press enter during message
        enterName.config(bg="#ffc6c2")
        enterName.config(state=DISABLED)
        printMessagePause("Invalid Name! Please Type a proper name",
                          "", 13, 0, 0, 0, 0.5, 0, 0, 0)
        time.sleep(0.3)
        enterName.config(state=NORMAL)
        enterName.focus()
        b1 = root.bind('<Return>', lambda x: submitName())


# def adminSetup():  # setup for admin button(skips beggining dialog and assumes name of "Gavin")
#     global name
#     name = "Gavin"
#     startButton.place_forget()
#     noTextPlay.place_forget()
#     adminButton.place_forget()
#     startImageLabel.config(image=brickwall)
#     doRules(0)


def doRules(do):  # what happens when you choose to see the rules or not(for param "do": 1 = rules, 0 = no rules)
    global northBind
    global eastBind
    global southBind
    global westBind
    explainYes.place_forget()
    explainNo.place_forget()
    if do == 1:  # Creates small animation including buttons appearing one at a time, and flashing to show disabled state

        printMessage("Press North, ", "")
        northButton.place(x=170, y=270)
        root.update()
        time.sleep(0.8)

        printMessage("East, ", "Press North, ")
        eastButton.place(x=250, y=350)
        root.update()
        time.sleep(0.8)

        printMessage("South, ", "Press North, East, ")
        southButton.place(x=170, y=430)
        root.update()
        time.sleep(0.8)

        printMessage(" West, ", "Press North, East, South, ")
        westButton.place(x=90, y=350)
        root.update()
        time.sleep(0.8)

        printMessagePause(
            "to travel in that direction. If the button is gray",
            "Press North, East, South, West, ", 28, 0, 0, 0, 0.5, 0, 0, 0)
        directionsToggle(0, 0, 0, 0)
        printMessage("ed out that",
                     "Press North, East, South, West, to travel in that direction. If the button is gray")
        directionsToggle(1, 1, 1, 1)
        printMessage(" means the",
                     "Press North, East, South, West, to travel in that direction. If the button is grayed out that")
        directionsToggle(0, 0, 0, 0)
        printMessage("re is nowh",
                     "Press North, East, South, West, to travel in that direction. If the button is grayed out that means the")
        directionsToggle(1, 1, 1, 1)
        printMessagePause(
            "ere to go in that direction. Other buttons will appear depending on the situation(You can also use WASD).",
            "Press North, East, South, West, to travel in that direction. If the button is grayed out that means there is nowh",
            28, 81, 0, 0, 0.5, 0.5, 0, 0)
        time.sleep(2)
        printMessagePause(
            "The buttons will rotate so that which ever direction you are facing is the highest button(WASD will also shift so that W is always the top button, S is always the bottom, and so on and so forth).",
            "", 89, 146, 170, 0, 0.5, 0.5, 0.5, 0.5)
        time.sleep(2)
    elif do == 0:

        northButton.place(x=170, y=270)
        eastButton.place(x=250, y=350)
        southButton.place(x=170, y=430)
        westButton.place(x=90, y=350)

    imageLabel.place(x=480, y=216)  # Places Main game Image Frame
    facingLabel.place(x=148, y=571)  # places Compass
    plantation()


def unbinded():  # function to demonstrate that a key is unbinded
    print("Unbinded, this wasn't supposed to be pressed.")


class startGame():  # Has to have multiple phases to prevent game from continuing before required actions happenb
    global name

    def phase1():
        global b1
        startImageLabel.config(image=brickwall)
        startButton.place_forget()
        noTextPlay.place_forget()
        # adminButton.place_forget()

        printMessagePause("Hey, you! Welcome to The Long Lost Locks! What's your name?",
                          "", 4, 9, 41, 0, 0.5, 0.5, 0.5, 0)

        time.sleep(0.05)
        enterName.place(x=338, y=220)
        enterNameB.place(x=581, y=270)
        b1 = root.bind('<Return>', lambda x: submitName())
        enterName.focus()

    def phase2():
        sayName = name + "! What a cool name! Let's get started!"
        printMessagePause(sayName,
                          "", len(name) + 1, len(name) + 19, 0, 0, 0.5, 0.5, 0, 0)
        time.sleep(0.5)
        printMessage("Would you like me to explain the controls?", "")
        explainYes.place(x=118, y=220)
        explainNo.place(x=692, y=220)


def noTextSetup():  # Setup for no text. skips beginning dialog and doesn't show text throughout game
    global name
    global textPlay
    global beenPlantation
    global beenUpclose
    global beenField
    global beenVillage1
    global beenVillage2
    global beenVillage3
    global beenBunker
    global beenBaldbasementEntrance
    global beenHouseEntrance
    global beenLibrary
    global beenLivingRoom
    global beenUpstairs
    global beenSafeRoom
    global beenSafe
    global beenBackyard
    global beenBasement
    global beenCellar
    global beenSwamp
    global beenDojoExt
    global beenDojoInt
    global beenIntersection
    global beenJunkyard
    global beenJunkyardDeep
    global beenBlue
    global beenRed
    global beenGreen
    # global beenMonkeyMan # Don't do this one

    textPlay = False
    startButton.place_forget()
    noTextPlay.place_forget()
    # adminButton.place_forget()
    startImageLabel.config(image=brickwall)
    beenPlantation = True
    beenUpclose = True
    beenField = True
    beenVillage1 = True
    beenVillage2 = True
    beenVillage3 = True
    beenBunker = True
    beenBaldbasementEntrance = True
    beenLibrary = True
    beenHouseEntrance = True
    beenLivingRoom = True
    beenUpstairs = True
    beenSafeRoom = True
    beenSafe = True
    beenBackyard = True
    beenBasement = True
    beenCellar = True
    beenSwamp = True
    beenDojoExt = True
    beenDojoInt = True
    beenIntersection = True
    beenJunkyard = True
    beenJunkyardDeep = True
    beenBlue = True
    beenRed = True
    beenGreen = True
    # beenMonkeyMan = True < don't do this
    doRules(0)
    name = "Player"


def resetMenu():
    menuButton.place_forget()
    northButton.place_forget()
    eastButton.place_forget()
    southButton.place_forget()
    westButton.place_forget()
    imageLabel.place_forget()
    eventclear()
    startImageLabel.config(image=bgimage)
    startButton.place(x=789, y=252)
    noTextPlay.place(x=859, y=442)
    # adminButton.place(x=10, y=217)
    defaultVars()
    enterName.delete(0, END)


# ----------------------------#
# -----START OF GAME FUNCS----#
# ----------------------------#

def directionsToggle(toggleNorth, toggleEast, toggleSouth,
                     toggleWest):  # Some functions that make coding easier for later use
    if toggleNorth == 1:
        northButton.config(state=NORMAL, relief=RAISED, bg="#727882")
    elif toggleNorth == 0:
        northButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
        root.bind("<w>", lambda z: unbinded())

    if toggleEast == 1:
        eastButton.config(state=NORMAL, relief=RAISED, bg="#727882")
    elif toggleEast == 0:
        eastButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
        root.bind("<d>", lambda z: unbinded())
    if toggleSouth == 1:
        southButton.config(state=NORMAL, relief=RAISED, bg="#727882")
    elif toggleSouth == 0:
        southButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
        root.bind("<s>", lambda z: unbinded())
    if toggleWest == 1:
        westButton.config(state=NORMAL, relief=RAISED, bg="#727882")
    elif toggleWest == 0:
        westButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
        root.bind("<a>", lambda z: unbinded())


def disableDir():
    global northBind
    global eastBind
    global southBind
    global westBind
    northButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
    eastButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
    southButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
    westButton.config(state=DISABLED, relief=SUNKEN, bg="#f0f0f0")
    # root.unbind("<w>", northBind())
    root.bind("<w>", lambda z: unbinded())
    # root.unbind("<d>", eastBind())
    root.bind("<d>", lambda z: unbinded())
    # root.unbind("<s>", southBind())
    root.bind("<s>", lambda z: unbinded())
    # root.unbind("<a>", westBind())
    root.bind("<a>", lambda z: unbinded())


def setCommands(commandNorth, commandEast, commandSouth, commandWest):
    if 0 == commandNorth:
        commandNorth = unbinded
    if 0 == commandEast:
        commandEast = unbinded
    if 0 == commandSouth:
        commandSouth = unbinded
    if 0 == commandWest:
        commandWest = unbinded
    global northBind
    global eastBind
    global southBind
    global westBind
    northBind = root.bind("<w>", lambda x: commandNorth())
    northButton.config(command=commandNorth)
    eastBind = root.bind("<d>", lambda x: commandEast())
    eastButton.config(command=commandEast)
    southBind = root.bind("<s>", lambda x: commandSouth())
    southButton.config(command=commandSouth)
    westBind = root.bind("<a>", lambda x: commandWest())
    westButton.config(command=commandWest)


def setImage(whatimage):  # Shorthand to configure game image
    imageLabel.config(image=whatimage)


def eventclear():  # Empties the eventbar(text at top)
    eventLabel.config(text="")


def setDir(dir):
    beforeNorth = northButton.cget("command")
    beforeEast = eastButton.cget("command")
    beforeSouth = southButton.cget("command")
    beforeWest = westButton.cget("command")

    northButton.place_forget()  # WHEN WAKE UP MAKE ARROW ROTATING WORK
    eastButton.place_forget()
    southButton.place_forget()
    westButton.place_forget()
    if dir == "North":
        facingLabel.config(image=compassN)
        northButton.place(x=170, y=270)
        eastButton.place(x=250, y=350)
        southButton.place(x=170, y=430)
        westButton.place(x=90, y=350)

    elif dir == "East":
        facingLabel.config(image=compassE)
        northButton.place(x=90, y=350)
        eastButton.place(x=170, y=270)
        southButton.place(x=250, y=350)
        westButton.place(x=170, y=430)
    elif dir == "South":
        facingLabel.config(image=compassS)
        northButton.place(x=170, y=430)
        eastButton.place(x=90, y=350)
        southButton.place(x=170, y=270)
        westButton.place(x=250, y=350)
    elif dir == "West":
        facingLabel.config(image=compassW)
        northButton.place(x=250, y=350)
        eastButton.place(x=170, y=430)
        southButton.place(x=90, y=350)
        westButton.place(x=170, y=270)


def fixDir(dir):
    beforeNorth = northButton.cget("command")
    beforeEast = eastButton.cget("command")
    beforeSouth = southButton.cget("command")
    beforeWest = westButton.cget("command")
    if (dir) == "North":  # Sets WASD for facing North
        root.bind("<w>", beforeNorth)
        root.bind("<d>", beforeEast)
        root.bind("<s>", beforeSouth)
        root.bind("<a>", beforeWest)
    elif (dir) == "East":  # Sets WASD for facing East
        root.bind("<w>", beforeEast)
        root.bind("<d>", beforeSouth)
        root.bind("<s>", beforeWest)
        root.bind("<a>", beforeNorth)
    elif (dir) == "South":  # Sets WASD for facing South
        root.bind("<w>", beforeSouth)
        root.bind("<d>", beforeWest)
        root.bind("<s>", beforeNorth)
        root.bind("<a>", beforeEast)
    elif (dir) == "West":  # Sets WASD for facing West
        root.bind("<w>", beforeWest)
        root.bind("<d>", beforeNorth)
        root.bind("<s>", beforeEast)
        root.bind("<a>", beforeSouth)


def knock():
    global firstBunkerAsk
    global inAskingPhase
    global hasKnocked
    global textPlay

    hasKnocked = True
    knockButton.place_forget()
    disableDir()
    root.bind("<s>", lambda g: unbinded())
    root.update()
    time.sleep(2)
    setImage(bunkerOpenImage)
    if textPlay == True:
        printMessage("What's the password?", "Lucas: ")
    else:
        eventLabel.config(text="Lucas: What's the password?")

    enterPassword.focus()
    enterPassword.place(x=528, y=261)
    enterPassword.delete(0, END)
    submitPassword.place(x=545, y=304)
    root.bind('<Return>', lambda x: submitPass())


def submitPass():
    global firstPassword
    global hasGreen
    global inAskingPhase
    if password == enterPassword.get().lower():
        if textPlay == True:
            printMessage("Here's your damn key.", "Lucas: ")
        else:
            eventLabel.config(text="Lucas: Here's your damn key.")

        time.sleep(0.5)
        setImage(greenkeyImage)
        root.update()
        hasGreen = True
        enterPassword.place_forget()
        submitPassword.place_forget()
        root.bind('<Return>', lambda x: unbinded())
        time.sleep(1.5)
        village3()
    else:
        wrongPassEnding()


def crackSafe():
    global password
    global safeCracked
    crackButton.place_forget()
    setImage(safeOpenImage)
    disableDir()
    if textPlay == True:
        printMessagePause(("The password for this run is is: " + password), "", 32, 0, 0, 0, 0.5, 0, 0, 0)
    else:
        eventLabel.config(text=("The password for this run is: " + password))
    directionsToggle(0, 0, 1, 0)
    setCommands(0, 0, safeRoom, 0)
    safeCracked = True


def dig():
    global hasBlue
    global textPlay
    digButton.place_forget()
    disableDir()
    setImage(bluekeyImage)
    if textPlay == True:
        printMessage("You found the Blue Key!", "")
    else:
        eventLabel.config(text="+ Blue Key")
    directionsToggle(0, 0, 1, 0)
    setCommands(0, 0, livingroom, 0)
    hasBlue = True


def grabOranges():
    global hasOranges
    global TextPlay
    orangesButton.place_forget()
    disableDir()
    if textPlay == True:
        printMessagePause("Wow, greedy you. There's no way you can eat ALL of those", "", 4, 16, 0, 0, 0.5, 0.5, 0, 0)
    else:
        eventLabel.config(text="+ Oranges")
    setDir("East")
    directionsToggle(0, 0, 0, 1)
    setCommands(0, 0, 0, basement)
    fixDir("East")
    hasOranges = True


def getShovel():
    global hasShovel
    global textPlay
    shovelButton.place_forget()
    setImage(noShovelImage)
    disableDir()
    if textPlay == True:
        printMessagePause("What? Seriously? What are you going to do with a shovel?", "", 5, 16, 0, 0, 0.5, 0.5, 0, 0)
    else:
        eventLabel.config(text="+ Shovel")
    setDir("East")
    directionsToggle(0, 0, 0, 1)
    setCommands(0, 0, 0, intersection)
    fixDir("East")
    hasShovel = True


def giveOranges():
    global hasRed
    global textPlay
    giveOrangesButton.place_forget()
    disableDir()
    setImage(redkeyImage)
    if textPlay == True:
        printMessage("You found the Red Key!", "")
    else:
        eventLabel.config(text="+ Red Key")
    setDir("West")

    directionsToggle(0, 1, 0, 0)
    setCommands(0, intersection, 0, 0)
    fixDir("West")
    hasRed = True


def openBlue():
    global hasBlue
    global textPlay
    global blueOpen
    blueDoorButton.place_forget()
    setImage(blueopenImage)
    disableDir()
    if textPlay == True:
        printMessage("Blue Door opened.", "")
    else:
        eventLabel.config(text="Blue Door opened.")
    blueOpen = True
    setDir("East")
    directionsToggle(0, 1, 0, 1)
    setCommands(0, redDoor, 0, swamp)
    fixDir("East")


def openRed():
    global hasRed
    global textPlay
    global redOpen
    redDoorButton.place_forget()
    setImage(redopenImage)
    disableDir()
    if textPlay == True:
        printMessage("Red Door opened.", "")
    else:
        eventLabel.config(text="Red Door opened.")
    redOpen = True
    setDir("East")
    directionsToggle(0, 1, 0, 1)
    setCommands(0, greenDoor, 0, blueDoor)
    fixDir("East")


def openGreen():
    global hasGreen
    global textPlay
    global greenOpen
    greenDoorButton.place_forget()
    setImage(greenopenImage)
    disableDir()
    if textPlay == True:
        printMessage("Green Door opened.", "")
    else:
        eventLabel.config(text="Green Door opened.")
    greenOpen = True
    setDir("East")
    directionsToggle(0, 1, 0, 1)
    setCommands(0, bossfight, 0, redDoor)
    fixDir("East")


# ----------------------------------#
# ------START OF LOCATION FUNCS-----#
# ----------------------------------#


def plantation():
    global firstTimePlantation
    global beenPlantation
    if firstTimePlantation == True:
        firstTimePlantation = False
    else:
        setDir("North")
    eventclear()
    setImage(plantationImage)
    if beenPlantation == False:
        disableDir()
        printMessagePause(
            "In search of the long lost patch of hair from the top of your head, you find yourself in a forest surrounded by...",
            "", 68, 113, 114, 115, 0.5, 0.2, 0.2, 0.2)
        printMessagePause(" Bananas... Hmm, interesting",
                          "In search of the long lost patch of hair from the top of your head, you find yourself in a forest surrounded by...",
                          9, 10, 11,
                          16, 0.2, 0.2, 0.2, 0.5)
        printMessagePause(". This isn't where your missing hair is...",
                          "In search of the long lost patch of hair from the top of your head, you find yourself in a forest surrounded by... Bananas... Hmm, interesting",
                          1, 40, 41,
                          42, 0.5, 0.2, 0.2, 0.2)
        beenPlantation = True
    directionsToggle(1, 0, 1, 0)
    setCommands(field, 0, upclose, 0)
    fixDir("North")


def upclose():
    global beenUpclose
    setDir("North")  # Creates exception so that the compass doesnt flip when you come close but
    facingLabel.config(image=compassS)  # the text will still say facing south
    eventclear()
    setImage(plantationcloseImage)
    if beenUpclose == False:
        disableDir()
        printMessagePause(
            (
                    "Oh, hello " + name + ", you look very excited about this totally non-mundane setting for an \"adventure\" game!"),
            "", 3,
            11 + len(name), 92 + len(name), 0, 0.5, 0.5, 0.7, 0)
        beenUpclose = True
    directionsToggle(1, 0, 0, 0)
    setCommands(plantation, 0, 0, 0)
    # fixDir() dont put this here! it is an exception!


def field():
    global beenField
    setDir("North")
    eventclear()
    setImage(fieldImage)
    if beenField == False:
        disableDir()
        printMessagePause("Ahhh, what a beautiful scene with filled with... absolutely nothing.", "", 5, 46, 47, 48,
                          0.5, 0.2, 0.2, 0.2)
        beenField = True
    directionsToggle(1, 1, 1, 1)
    setCommands(housefront, swamp, plantation, village1)
    fixDir("North")


def village1():
    global beenVillage1
    eventclear()
    setDir("West")
    setImage(village1Image)
    if beenVillage1 == False:
        disableDir()
        printMessage("You find your self a neat little village that has some neat little buildings.", "")
        beenVillage1 = True
    directionsToggle(1, 1, 1, 1)

    setCommands(library, field, baldbasementEntrance, village2)
    fixDir("West")


def village2():
    global beenVillage2
    eventclear()
    setDir("West")
    setImage(village2Image)
    if beenVillage2 == False:
        disableDir()
        printMessage("Off you go!", "")
        beenVillage2 = True
    directionsToggle(0, 1, 0, 1)

    setCommands(0, village1, 0, village3)
    fixDir("West")


def village3():
    global beenVillage3
    knockButton.place_forget()
    enterPassword.place_forget()
    submitPassword.place_forget()
    root.bind('<Return>', lambda x: unbinded())
    eventclear()
    setDir("West")
    setImage(village3Image)
    if beenVillage3 == False:
        disableDir()
        printMessage("Just a little bit further!", "")
        beenVillage3 = True
    directionsToggle(0, 1, 0, 1)
    if hasGreen == False:
        setCommands(0, village2, 0, bunker)
    else:
        setCommands(0, village2, 0, 0)
    fixDir("West")


def bunker():
    global beenBunker
    global hasGreen

    eventclear()
    setDir("West")

    if beenBunker == False:
        disableDir()
        printMessage("Who the hell built a bunker here?", "")
        beenBunker = True
    if (hasKnocked == False):
        setImage(bunkerImage)
    else:
        setImage(bunkerOpenImage)
    knockButton.place(x=528, y=261)
    directionsToggle(0, 0, 0, 0)

    setCommands(0, 0, 0, 0)
    fixDir("West")


def baldbasementEntrance():
    global beenBaldbasementEntrance
    eventclear()
    setDir("South")
    setImage(baldentranceImage)
    if beenBaldbasementEntrance == False:
        disableDir()
        printMessagePause("Oohhh, spooky, a basement, no way this could lead to something bad, could it?", "", 7, 14,
                          26, 67, 0.5, 0.5, 0.5, 0.5)
        beenBaldbasementEntrance = True
    directionsToggle(1, 0, 1, 0)

    setCommands(village1, 0, baldEnding, 0)
    fixDir("South")


def library():
    global beenLibrary
    global hasKnowledge
    global textPlay
    eventclear()
    setDir("North")
    setImage(libraryImage)
    if beenLibrary == False:
        disableDir()
        printMessagePause(
            "It's been 3 hours. You read an entire book on how to crack safes. Why didn't you just find one about picking locks? You could have just picked all three locks in the castle.",
            "", 18, 65, 115, 0, 0.5, 0.5, 0.5, 0)
        hasKnowledge = True
        beenLibrary = True
    directionsToggle(0, 0, 1, 0)
    if (textPlay == False) and (hasKnowledge == False):
        hasKnowledge = True
        eventLabel.config(text="+ Safe Cracking Knowledge")
    setCommands(0, 0, village1, 0)
    fixDir("North")


def housefront():
    global beenHouseEntrance
    eventclear()
    setDir("North")
    setImage(farmHouseEntranceImage)
    if beenHouseEntrance == False:
        disableDir()
        printMessage("Why the hell does everyone here leave their doors wide open?", "")
        beenHouseEntrance = True
    directionsToggle(1, 0, 1, 0)
    setCommands(livingroom, 0, field, 0)
    fixDir("North")


def livingroom():
    global beenLivingRoom
    digButton.place_forget()
    eventclear()
    setDir("North")
    setImage(livingroomImage)
    if beenLivingRoom == False:
        disableDir()
        printMessagePause("What a nice house! 2 floors, a basement, and a backyard!", "", 18, 28, 40, 0, 0.5, 0.5, 0.5,
                          0)
        beenLivingRoom = True
    directionsToggle(1, 1, 1, 1)
    setCommands(backyard, basement, housefront, upstairs)
    fixDir("North")


def upstairs():
    global beenUpstairs
    eventclear()
    setDir("North")
    setImage(upstairsImage)
    if beenUpstairs == False:
        disableDir()
        printMessagePause("Uh-oh, you'd better hope nobody's home.", "", 6, 0, 0, 0, 0.5, 0, 0, 0)
        beenUpstairs = True
    directionsToggle(1, 1, 0, 1)
    setCommands(safeRoom, livingroom, 0, angryManEnding)
    fixDir("North")


def safeRoom():
    global beenSafeRoom
    crackButton.place_forget()
    eventclear()
    setDir("North")
    setImage(safeRoomImage)
    if beenSafeRoom == False:
        disableDir()
        printMessagePause("Don't even think about it... ", "", 26, 27, 28, 0, 0.2, 0.2, 0.2, 0)
        beenSafeRoom = True
    directionsToggle(1, 0, 1, 0)
    setCommands(safe, 0, upstairs, 0)
    fixDir("North")


def safe():
    global beenSafe
    global safeCracked
    global hasKnowledge
    eventclear()
    setDir("North")
    if safeCracked == False:
        setImage(safeImage)
    else:
        setImage(safeOpenImage)
        eventLabel.config(text=("The password for this run is: " + password))
    if beenSafe == False:
        disableDir()
        printMessage("Do you even know how to open that thing?", "")
        print("hifff")
        beenSafe = True
    if (safeCracked == False) and (hasKnowledge == True):
        crackButton.place(x=528, y=261)
    directionsToggle(0, 0, 1, 0)
    setCommands(0, 0, safeRoom, 0)
    fixDir("North")


def backyard():
    global beenBackyard
    global hasShovel
    global hasBlue

    eventclear()
    setDir("North")
    if hasBlue == False:
        setImage(backyardImage)
    else:
        setImage(backyardHoleImage)
    if beenBackyard == False:
        disableDir()
        printMessage("What's the point of a fence when they have like 100 acres of land?", "")
        beenBackyard = True
    if (hasShovel == True) and (hasBlue == False):
        digButton.place(x=528, y=261)
    directionsToggle(0, 0, 1, 0)
    setCommands(0, 0, livingroom, 0)
    fixDir("North")


def basement():
    global beenBasement
    orangesButton.place_forget()
    eventclear()
    setDir("East")
    setImage(basementImage)
    if beenBasement == False:
        disableDir()
        printMessage("Does this house have any furniture?", "")
        beenBasement = True

    directionsToggle(0, 1, 0, 1)
    setCommands(0, cellar, 0, livingroom)
    # else:
    #     directionsToggle(0, 0, 0, 1)
    #     setCommands(0, 0, 0, livingroom)
    fixDir("East")


def cellar():
    global beenCellar
    global hasOranges
    eventclear()
    if hasOranges == False:
        orangesButton.place(x=528, y=261)
    setDir("East")
    setImage(cellarImage)
    if beenCellar == False:
        disableDir()
        printMessagePause("Oooh, yum! Oranges!", "", 5, 10, 19, 0, 0.5, 0.5, 0.5, 0)
        beenCellar = True
    directionsToggle(0, 0, 0, 1)
    setCommands(0, 0, 0, basement)
    fixDir("East")


def swamp():
    global beenSwamp
    blueDoorButton.place_forget()
    eventclear()
    setDir("East")
    setImage(swampImage)
    if beenSwamp == False:
        disableDir()
        printMessagePause("Eww Yuck, I'm the narrator and I still feel your disgust. ", "", 9, 0, 0, 0, 0.5, 0, 0, 0)
        beenSwamp = True
    directionsToggle(1, 1, 1, 1)
    setCommands(dojoExt, blueDoor, intersection, field)
    fixDir("East")


def dojoExt():
    global beenDojoExt
    eventclear()
    setDir("North")
    setImage(dojoExtImage)
    if beenDojoExt == False:
        disableDir()
        printMessagePause("Uh oh.. I'm getting a bad feeling about you being here.", "", 6, 7, 0, 0, 0.2, 0.2, 0, 0)
        beenDojoExt = True
    directionsToggle(1, 0, 1, 0)
    setCommands(dojoInt, 0, swamp, 0)
    fixDir("North")


def dojoInt():
    global beenDojoInt
    global hasKO
    global textPlay
    eventclear()
    setDir("North")
    setImage(dojoIntImage)
    if beenDojoInt == False:
        disableDir()
        printMessagePause(
            "Did you just teach yourself a marshall art in 2 hours without anyone's help? Good on you, I guess..",
            "", 76, 89, 98, 99, 0.5, 0.5, 0.2, 0.2)
        hasKO = True
        beenDojoInt = True
    directionsToggle(0, 0, 1, 0)
    if (textPlay == False) and (hasKO == False):
        hasKO = True
        eventLabel.config(text="+ KO Ability")
    setCommands(0, 0, dojoExt, 0)
    fixDir("North")


def intersection():
    global beenIntersection
    eventclear()
    giveOrangesButton.place_forget()
    setDir("South")
    setImage(leavingSwampImage)
    if beenIntersection == False:
        disableDir()
        printMessagePause("Finally were out of -- Hey, I recognise that guy, who is he again? ", "", 21, 21, 27, 49,
                          0.25, 0.25, 0.5, 0.5)
        beenIntersection = True
    directionsToggle(1, 1, 0, 1)
    setCommands(swamp, junkyard, 0, duo)
    fixDir("South")


def duo():
    global beenMonkeyMan
    global hasOranges
    global textPlay
    global hasRed
    eventclear()
    setDir("West")
    setImage(curiousGeorgeImage)
    if (beenMonkeyMan == True) and (hasOranges == False):
        monkeyEnding()
        return
    if (hasOranges == True) and (hasRed == False):
        giveOrangesButton.place(x=528, y=261)
    if (beenMonkeyMan == False) and (hasRed == False):
        disableDir()
        if (textPlay == True):
            printMessagePause(
                "Hey, do you think you could help bring us some food? It's gotten to the point where even my monkey is sick of these bananas. Maybe some oranges or something?",
                "Yellow Hat Man: ", 4, 124, 0, 0, 0.5, 0.5, 0, 0)
        else:
            eventLabel.config(text="Yellow Hat Man: Bring us oranges please")
        beenMonkeyMan = True

    directionsToggle(0, 1, 0, 0)
    setCommands(0, intersection, 0, 0)
    fixDir("West")


def junkyard():
    global beenJunkyard
    global hasKO
    global hasShovel
    shovelButton.place_forget()
    eventclear()
    setDir("East")
    if hasKO == True:
        setImage(deadyardImage)
    else:
        arrestedEnding()
        return
    if beenJunkyard == False:
        disableDir()
        printMessage("You used your new found martial arts skills to KO the yard owner before he could call the cops.",
                     "")
        beenJunkyard = True
    directionsToggle(0, 1, 0, 1)
    setCommands(0, junkyardDeep, 0, intersection)

    fixDir("East")


def junkyardDeep():
    global beenJunkyardDeep
    global hasShovel
    eventclear()
    if hasShovel == False:
        shovelButton.place(x=528, y=261)
        setImage(junkpileImage)
    else:
        setImage(noShovelImage)
    setDir("East")

    if beenJunkyardDeep == False:
        disableDir()
        printMessage("Why is the junkyard full of junk?", "")
        beenJunkyardDeep = True
    directionsToggle(0, 0, 0, 1)
    setCommands(0, 0, 0, junkyard)
    fixDir("East")


def blueDoor():
    global hasBlue
    global beenBlue
    global blueOpen
    eventclear()
    redDoorButton.place_forget()
    setDir("East")
    if blueOpen == False:
        setImage(bluedoorImage)
    else:
        setImage(blueopenImage)
    if beenBlue == False:
        disableDir()
        printMessage("You need a blue key to open this door.", "")
        beenBlue = True
    if ((textPlay == False) or (beenBlue == True)) and (blueOpen == False):
        eventLabel.config(text="You need a blue key to open this door.")
    elif ((textPlay == False) or (beenBlue == True)) and (blueOpen == True):
        eventLabel.config(text="Blue Door opened.")
    if (blueOpen == False) and (hasBlue == True):
        blueDoorButton.place(x=528, y=261)
    if blueOpen == False:
        directionsToggle(0, 0, 0, 1)
        setCommands(0, 0, 0, swamp)
    else:
        directionsToggle(0, 1, 0, 1)
        setCommands(0, redDoor, 0, swamp)
    fixDir("East")


def redDoor():
    global hasRed
    global beenRed
    global redOpen
    eventclear()
    greenDoorButton.place_forget()
    blueDoorButton.place_forget()
    setDir("East")
    if redOpen == False:
        setImage(reddoorImage)
    else:
        setImage(redopenImage)
    if beenRed == False:
        disableDir()
        printMessage("You need a red key to open this door.", "")
        beenRed = True
    if ((textPlay == False) or (beenRed == True)) and (redOpen == False):
        eventLabel.config(text="You need a red key to open this door.")
    elif ((textPlay == False) or (beenRed == True)) and (redOpen == True):
        eventLabel.config(text="Red Door opened.")
    if (redOpen == False) and (hasRed == True):
        redDoorButton.place(x=528, y=261)
    if redOpen == False:
        directionsToggle(0, 0, 0, 1)
        setCommands(0, 0, 0, blueDoor)
    else:
        directionsToggle(0, 1, 0, 1)
        setCommands(0, greenDoor, 0, blueDoor)
    fixDir("East")


def greenDoor():
    global hasGreen
    global beenGreen
    global greenOpen
    eventclear()
    redDoorButton.place_forget()
    setDir("East")
    if greenOpen == False:
        setImage(greendoorImage)
    else:
        setImage(greenopenImage)
    if beenGreen == False:
        disableDir()
        printMessage("You need a green key to open this door.", "")
        beenGreen = True
    if ((textPlay == False) or (beenGreen == True)) and (greenOpen == False):
        eventLabel.config(text="You need a green key to open this door.")
    elif ((textPlay == False) or (beenGreen == True)) and (greenOpen == True):
        eventLabel.config(text="Green Door opened.")
    if (greenOpen == False) and (hasGreen == True):
        greenDoorButton.place(x=528, y=261)
    if greenOpen == False:
        directionsToggle(0, 0, 0, 1)
        setCommands(0, 0, 0, redDoor)
    else:
        directionsToggle(0, 1, 0, 1)
        setCommands(0, bossfight, 0, redDoor)
    fixDir("East")


def bossfight():
    global textPlay
    redDoorButton.place_forget()
    disableDir()
    setImage(dragonFightImage)
    if textPlay == True:
        printMessage("Time for the great dragon fight!", "")
    throwOrange.place(x=528, y=261)
    judoAttack.place(x=528, y=301)


# ---------------------------#
# ------START OF ENDINGS-----#
# ---------------------------#

def baldEnding():
    facingLabel.place_forget()
    setImage(baldbasementImage)
    disableDir()
    printMessagePause(
        "You lost! The vault door slams closed behind you, and all of what little hair you had left is yanked out of your scalp by a group of small, angry, malnourished elves.",
        "", 9, 49, 139, 146, 0.7, 0.5, 0.5, 0.5)
    menuButton.place(x=41, y=533)


def wrongPassEnding():
    facingLabel.place_forget()
    enterPassword.place_forget()
    submitPassword.place_forget()
    printMessagePause("You lost. You only get one shot at the password.", "", 9, 0, 0, 0, 0.5, 0, 0, 0)
    menuButton.place(x=41, y=533)


def angryManEnding():
    facingLabel.place_forget()
    setImage(angrymanImage)
    disableDir()
    printMessagePause(
        "This should be a lesson to never intrude into someone's house! What the hell were you doing anyways?",
        "", 62, 0, 0, 0, 0.5, 0, 0, 0)
    menuButton.place(x=41, y=533)


def monkeyEnding():
    global name
    facingLabel.place_forget()
    disableDir()
    printMessagePause("I didn't want to have to do this, but my monkey is really hungry, sorry.", "Yellow Hat Man: ",
                      33, 65, 72, 0, 0.5, 0.5, 0.5, 0)
    time.sleep(1.5)
    setImage(monkeyEatImage)
    printMessagePause(
        ("RIP " + name + ". You were a real snack."),
        "", len(name) + 5, 0, 0, 0, 0.5, 0, 0, 0)

    menuButton.place(x=41, y=533)


def arrestedEnding():
    facingLabel.place_forget()
    disableDir()
    setImage(arrestedImage)
    printMessagePause(
        (
            "The yard owner called the cops and they came right away to arrest you for the most felonious crime possible: Trespassing on a landfill."),
        "", 108, 0, 0, 0, 0.7, 0, 0, 0)

    menuButton.place(x=41, y=533)


def winEnding():
    facingLabel.place_forget()
    throwOrange.place_forget()
    judoAttack.place_forget()
    setImage(winImage)
    printMessagePause(
        "You won! The dragon died of his deadly allergy to oranges, leaving you access to his secret layer behind where he sleeps, stocked full of fresh hair.",
        "", 8, 58, 121, 0, 0.5, 0.5, 0.5, 0)
    menuButton.place(x=41, y=533)


def dragonEnding():
    facingLabel.place_forget()
    throwOrange.place_forget()
    judoAttack.place_forget()
    setImage(bigLossImage)
    printMessagePause(
        "Why did you think that would work? You know dragons can fly right? The dragon had no intentions to hurt you but he retaliated by scorching all of your remaining hair off.",
        "", 34, 66, 0, 0, 0.5, 0.5, 0, 0)
    menuButton.place(x=41, y=533)


# ------------------------------------#
# ------START OF WIDGET DECLARING-----#
# ------------------------------------#

northButton = Button(root, text="North", width=9, height=4, bg="#727882", activebackground="#727882")
eastButton = Button(root, text="East", width=9, height=4, bg="#727882", activebackground="#727882")
southButton = Button(root, text="South", width=9, height=4, bg="#727882", activebackground="#727882")
westButton = Button(root, text="West", width=9, height=4, bg="#727882", activebackground="#727882")

explainYes = Button(root, text="Yes", bg="#05a64b", command=lambda: doRules(1), font=("", 30), width=20, height=4)
explainNo = Button(root, text="No", bg="#961b12", command=lambda: doRules(0), font=("", 30), width=20, height=4)
enterName = Entry(root, width=40, justify=CENTER, font=("", 20))
enterNameB = Button(root, text="Confirm", bg="#05a64b", command=submitName, font=("", 20))

startImageLabel = Label(root, image=bgimage, bg="black", borderwidth=0)
startImageLabel.place(x=0, y=197)
startImageLabel.lower()
startButton = Button(root, text="Start Game", command=startGame.phase1, width=20, height=3, font=("", 30),
                     bg="#05a64b")  # Should start at phase 1, revert to phase 1 once coding is done
startButton.place(x=789, y=252)

noTextPlay = Button(root, text="Play without text", command=noTextSetup, bg="#cf8a1b", width=20, height=3,
                    font=("", 20))
noTextPlay.place(x=859, y=442)

# adminButton = Button(root, text="Admin", command=adminSetup, bg="#e05e5e", width=20, height=3, font=("", 15))
# adminButton.place(x=10, y=217)

imageLabel = Label(root, image=plantationImage, borderwidth=0)
facingLabel = Label(root, image=compassN, borderwidth=0)

menuButton = Button(root, width=20, height=3, font=("", 20), text="Back to Menu", bg="#a31903", command=resetMenu)

knockButton = Button(root, width=20, height=3, text="Knock", command=knock, bg="#727882", activebackground="#727882")
enterPassword = Entry(root, width=30)
submitPassword = Button(root, width=20, command=submitPass, text="Submit", bg="#727882", activebackground="#727882")
crackButton = Button(root, width=20, command=crackSafe, text="Crack Safe", bg="#727882", activebackground="#727882")
digButton = Button(root, width=20, command=dig, text="Dig", bg="#727882", activebackground="#727882")
orangesButton = Button(root, width=20, command=grabOranges, text="Grab Some Oranges", bg="#727882",
                       activebackground="#727882")
giveOrangesButton = Button(root, width=20, command=giveOranges, text="Give Oranges", bg="#727882",
                           activebackground="#727882")
shovelButton = Button(root, width=20, command=getShovel, text="Pick Up Shovel", bg="#727882",
                      activebackground="#727882")
blueDoorButton = Button(root, width=20, command=openBlue, text="Open Blue Door", bg="#083480",
                        activebackground="#083480", fg="white")
redDoorButton = Button(root, width=20, command=openRed, text="Open Red Door", bg="#800808",
                       activebackground="#800808", fg="white")
greenDoorButton = Button(root, width=20, command=openGreen, text="Open Green Door", bg="#0e8008",
                         activebackground="#0e8008", fg="white")
throwOrange = Button(root, width=20, command=winEnding, text="Throw some Oranges", bg="#727882",
                     activebackground="#727882", fg="white")
judoAttack = Button(root, width=20, command=dragonEnding, text="Judo Attack", bg="#727882",
                    activebackground="#727882", fg="white")


# -------------------------------------------------#
# ------START OF MAJORITY VARIABLE DECLARATION-----#
# -------------------------------------------------#

wordlist = ("aaron","abandoned","aberdeen",
"abilities","ability","able","aboriginal","about","above","abraham","abroad",
"absence","absent","absolute","absolutely","absorption","abstract","abstracts",
"abuse","academic","academics","academy","accent","accept","acceptable","acceptance",
"accepted","accepting","accepts","access","accessed","accessibility","accessible","accessing",
"accessories","accessory","accident","accidents","accommodate","accommodation","accommodations","accompanied",
"accompanying","accomplish","accomplished","accordance","according","accordingly","account","accountability",
"accounting","accounts","accreditation","accredited","accuracy","accurate","accurately","accused",
"acdbentity","acer","achieve","achieved","achievement","achievements","achieving","acid",
"acids","acknowledge","acknowledged","acne","acoustic","acquire","acquired","acquisition",
"acquisitions","acre","acres","acrobat","across","acrylic","acting","action",
"actions","activated","activation","active","actively","activists","activities","activity",
"actor","actors","actress","acts","actual","actually","acute","adam",
"adams","adaptation","adapted","adapter","adapters","adaptive","adaptor","added",
"addiction","adding","addition","additional","additionally","additions","address","addressed",
"addresses","addressing","adds","adelaide","adequate","adidas","adipex","adjacent",
"adjust","adjustable","adjusted","adjustment","adjustments","admin","administered","administration",
"administrative","administrator","administrators","admission","admissions","admit","admitted","adobe",
"adolescent","adopt","adopted","adoption","adrian","adsl","adult","adults",
"advance","advanced","advancement","advances","advantage","advantages","adventure","adventures",
"adverse","advert","advertise","advertisement","advertisements","advertiser","advertisers","advertising",
"advice","advise","advised","advisor","advisors","advisory","advocacy","advocate",
"adware","aerial","aerospace","affair","affairs","affect","affected","affecting",
"affects","affiliate","affiliated","affiliates","affiliation","afford","affordable","afghanistan",
"afraid","africa","african","after","afternoon","afterwards","again","against",
"aged","agencies","agency","agenda","agent","agents","ages","aggregate",
"aggressive","aging","agree","agreed","agreement","agreements","agrees","agricultural",
"agriculture","ahead","aids","aimed","aims","aircraft","airfare","airline",
"airlines","airplane","airport","airports","alabama","alan","alarm","alaska",
"albania","albany","albert","alberta","album","albums","albuquerque","alcohol",
"alert","alerts","alex","alexander","alexandria","alfred","algebra","algeria",
"algorithm","algorithms","alias","alice","alien","align","alignment","alike",
"alive","allah","allan","alleged","allen","allergy","alliance","allied",
"allocated","allocation","allow","allowance","allowed","allowing","allows","alloy",
"almost","alone","along","alot","alpha","alphabetical","alpine","already",
"also","alter","altered","alternate","alternative","alternatively","alternatives","although",
"alto","aluminium","aluminum","alumni","always","amanda","amateur","amazing",
"amazon","amazoncom","amazoncouk","ambassador","amber","ambien","ambient","amend",
"amended","amendment","amendments","amenities","america","american","americans","americas",
"amino","among","amongst","amount","amounts","ampland","amplifier","amsterdam",
"anaheim","analog","analyses","analysis","analyst","analysts","analytical",
"analyze","analyzed","anatomy","anchor","ancient","andale","anderson","andorra",
"andrea","andreas","andrew","andrews","andy","angel","angela","angeles",
"angels","anger","angle","angola","angry","animal","animals","animated",
"animation","anime","anna","anne","annex","annie","anniversary","annotated",
"annotation","announce","announced","announcement","announcements","announces","annoying","annual",
"annually","anonymous","another","answer","answered","answering","answers","antarctica",
"antenna","anthony","anthropology","anti","antibodies","antibody","anticipated","antigua",
"antique","antiques","antivirus","antonio","anxiety","anybody","anymore","anyone",
"anything","anytime","anyway","anywhere","apache","apart","apartment","apartments",
"apnic","apollo","apparatus","apparel","apparent","apparently","appeal","appeals",
"appear","appearance","appeared","appearing","appears","appendix","apple","appliance",
"appliances","applicable","applicant","applicants","application","applications","applied","applies",
"apply","applying","appointed","appointment","appointments","appraisal","appreciate","appreciated",
"appreciation","approach","approaches","appropriate","appropriations","approval","approve","approved",
"approx","approximate","approximately","apps","april","aqua","aquarium","aquatic",
"arab","arabia","arabic","arbitrary","arbitration","arcade","arch","architect",
"architects","architectural","architecture","archive","archived","archives","arctic","area",
"areas","arena","argentina","argue","argued","argument","arguments","arise",
"arising","arizona","arkansas","arlington","armed","armenia","armor","arms",
"armstrong","army","arnold","around","arrange","arranged","arrangement","arrangements",
"array","arrest","arrested","arrival","arrivals","arrive","arrived","arrives",
"arrow","arthritis","arthur","article","articles","artificial","artist","artistic",
"artists","arts","artwork","aruba","asbestos","ascii","ashley","asia",
"asian","aside","asin","asked","asking","asks","aspect","aspects",
"aspnet","assault","assembled","assembly","assess","assessed","assessing","assessment",
"assessments","asset","assets","assign","assigned","assignment","assignments","assist",
"assistance","assistant","assisted","assists","associate","associated","associates","association",
"associations","assume","assumed","assumes","assuming","assumption","assumptions","assurance",
"assure","assured","asthma","astrology","astronomy","asus","athens","athletes",
"athletic","athletics","atlanta","atlantic","atlas","atmosphere","atmospheric","atom",
"atomic","attach","attached","attachment","attachments","attack","attacked","attacks",
"attempt","attempted","attempting","attempts","attend","attendance","attended","attending",
"attention","attitude","attitudes","attorney","attorneys","attract","attraction","attractions",
"attractive","attribute","attributes","auburn","auckland","auction","auctions","audi",
"audience","audio","audit","auditor","august","aurora","austin","australia",
"australian","austria","authentic","authentication","author","authorities","authority","authorization",
"authorized","authors","auto","automated","automatic","automatically","automation","automobile",
"automobiles","automotive","autos","autumn","availability","available","avatar","avenue",
"average","aviation","avoid","avoiding","avon","award","awarded","awards",
"aware","awareness","away","awesome","awful","axis","azerbaijan","babe",
"babes","babies","baby","bachelor","back","backed","background","backgrounds",
"backing","backup","bacon","bacteria","bacterial","badge","badly","baghdad",
"bags","bahamas","bahrain","bailey","baker","baking","balance","balanced",
"bald","bali","ball","ballet","balloon","ballot","balls","baltimore",
"banana","band","bands","bandwidth","bang","bangbus","bangkok","bangladesh",
"bank","banking","bankruptcy","banks","banned","banner","banners","baptist",
"barbados","barbara","barbie","barcelona","bare","barely","bargain","bargains",
"barn","barnes","barrel","barrier","barriers","barry","bars","base",
"baseball","based","baseline","basement","basename","bases","basic","basically",
"basics","basin","basis","basket","basketball","baskets","bass","batch",
"bath","bathroom","bathrooms","baths","batman","batteries","battery","battle",
"battlefield","bdsm","beach","beaches","beads","beam","bean","beans",
"bear","bearing","bears","beast","beastality","beastiality","beat","beatles",
"beats","beautiful","beautifully","beauty","beaver","became","because","become",
"becomes","becoming","bedding","bedford","bedroom","bedrooms","beds","beef",
"been","beer","before","began","begin","beginner","beginners","beginning",
"begins","begun","behalf","behavior","behavioral","behaviour","behind","beijing",
"being","beings","belarus","belfast","belgium","belief","beliefs","believe",
"believed","believes","belize","belkin","bell","belle","belly","belong",
"belongs","below","belt","belts","bench","benchmark","bend","beneath",
"beneficial","benefit","benefits","benjamin","bennett","benz","berkeley","berlin",
"bermuda","bernard","berry","beside","besides","best","bestiality","bestsellers",
"beta","beth","better","betting","betty","between","beverage","beverages",
"beverly","beyond","bhutan","bias","bible","biblical","bibliographic","bibliography",
"bicycle","bidder","bidding","bids","bigger","biggest","bike","bikes",
"bikini","bill","billing","billion","bills","billy","binary","bind",
"binding","bingo","biodiversity","biographies","biography","biol","biological","biology",
"bios","biotechnology","bird","birds","birmingham","birth","birthday","bishop",
"bite","bits","bizarre","bizrate","black","blackberry","blackjack",
"blacks","blade","blades","blah","blair","blake","blame","blank",
"blanket","blast","bleeding","blend","bless","blessed","blind","blink",
"block","blocked","blocking","blocks","blog","blogger","bloggers","blogging",
"blogs","blond","blonde","blood","bloody","bloom","bloomberg","blow",
"blowing","blue","blues","bluetooth","blvd","board",
"boards","boat","boating","boats","bobby","bodies","body","bold",
"bolivia","bolt","bomb","bond","bondage","bonds","bone","bones",
"bonus","book","booking","bookings","bookmark","bookmarks",
"books","bookstore","bool","boolean","boom","boost","boot","booth",
"boots","booty","border","borders","bored","boring","born","borough",
"bosnia","boss","boston","both","bother","botswana","bottle","bottles",
"bottom","bought","boulder","boulevard","bound","boundaries","boundary","bouquet",
"boutique","bowl","bowling","boxed","boxes","boxing","boys","bracelet",
"bracelets","bracket","brad","bradford","bradley","brain","brake","brakes",
"branch","branches","brand","brandon","brands","bras","brass","brave",
"brazil","brazilian","breach","bread","break","breakdown","breakfast","breaking",
"breaks","breast","breasts","breath","breathing","breed","breeding","breeds",
"brian","brick","bridal","bride","bridge","bridges","brief","briefing",
"briefly","briefs","bright","brighton","brilliant","bring","bringing","brings",
"brisbane","bristol","britain","britannica","british","britney","broad","broadband",
"broadcast","broadcasting","broader","broadway","brochure","brochures","broke","broken",
"broker","brokers","bronze","brook","brooklyn","brooks","bros","brother",
"brothers","brought","brown","browse","browser","browsers","browsing","bruce",
"brunei","brunette","brunswick","brush","brussels","brutal","bryan","bryant",
"bubble","buck","bucks","budapest","buddy","budget","budgets","buffalo",
"buffer","bufing","bugs","build","builder","builders","building","buildings",
"builds","built","bukkake","bulgaria","bulgarian","bulk","bull","bullet",
"bulletin","bumper","bunch","bundle","bunny","burden","bureau","buried",
"burke","burlington","burn","burner","burning","burns","burst","burton",
"buses","bush","business","businesses","busty","busy","butler","butt",
"butter","butterfly","button","buttons","butts","buyer","buyers","buying",
"buys","buzz","byte","bytes","cabin","cabinet","cabinets","cable",
"cables","cache","cached","cadillac","cafe","cage","cake","cakes",
"calcium","calculate","calculated","calculation","calculations","calculator","calculators","calendar",
"calendars","calgary","calibration","calif","california","call","called","calling",
"calls","calm","calvin","cambodia","cambridge","camcorder","camcorders","came",
"camel","camera","cameras","cameron","cameroon","camp","campaign","campaigns",
"campbell","camping","camps","campus","cams","canada","canadian","canal",
"canberra","cancel","cancellation","cancelled","cancer","candidate","candidates","candle",
"candles","candy","cannon","canon","cant","canvas","canyon","capabilities",
"capability","capable","capacity","cape","capital","capitol","caps","captain",
"capture","captured","carb","carbon","card","cardiac","cardiff","cardiovascular",
"cards","care","career","careers","careful","carefully","carey","cargo",
"caribbean","caring","carl","carlo","carlos","carmen","carnival","carol",
"carolina","caroline","carpet","carried","carrier","carriers","carries","carroll",
"carry","carrying","cars","cart","carter","cartoon","cartoons","cartridge",
"cartridges","casa","case","cases","casey","cash","cashiers","casino",
"casinos","casio","cassette","cast","casting","castle","casual","catalog",
"catalogs","catalogue","catalyst","catch","categories","category","catering","cathedral",
"catherine","catholic","cats","cattle","caught","cause","caused","causes",
"causing","caution","cave","cayman","cdna","cedar","ceiling","celebrate",
"celebration","celebrities","celebrity","celebs","cell","cells","cellular","celtic",
"cement","cemetery","census","cent","center","centered","centers","central",
"centre","centres","cents","centuries","century","ceramic","ceremony","certain",
"certainly","certificate","certificates","certification","certified","cest","chad","chain",
"chains","chair","chairman","chairs","challenge","challenged","challenges","challenging",
"chamber","chambers","champagne","champion","champions","championship","championships","chan",
"chance","chancellor","chances","change","changed","changelog","changes","changing",
"channel","channels","chaos","chapel","chapter","chapters","char","character",
"characteristic","characteristics","characterization","characterized","characters","charge","charged","charger",
"chargers","charges","charging","charitable","charity","charles","charleston","charlie",
"charlotte","charm","charming","charms","chart","charter","charts","chase",
"chassis","chat","cheap","cheaper","cheapest","cheat","cheats","check",
"checked","checking","checklist","checkout","checks","cheers","cheese","chef",
"chelsea","chem","chemical","chemicals","chemistry","chen","cheque","cherry",
"chess","chest","chester","chevrolet","chevy","chicago","chick","chicken",
"chicks","chief","child","childhood","children","childrens","chile","china",
"chinese","chip","chips","chocolate","choice","choices","choir","cholesterol",
"choose","choosing","chorus","chose","chosen","chris","christ","christian",
"christianity","christians","christina","christine","christmas","christopher","chrome","chronic",
"chronicle","chronicles","chrysler","chubby","chuck","church","churches","cialis",
"ciao","cigarette","cigarettes","cincinnati","cindy","cinema","cingular","circle",
"circles","circuit","circuits","circular","circulation","circumstances","circus","cisco",
"citation","citations","cite","cited","cities","citizen","citizens","citizenship",
"city","citysearch","civic","civil","civilian","civilization","claim","claimed",
"claims","claire","clan","clara","clarity","clark","clarke","class",
"classes","classic","classical","classics","classification","classified","classifieds","classroom",
"clause","clay","clean","cleaner","cleaners","cleaning","cleanup","clear",
"clearance","cleared","clearing","clearly","clerk","cleveland","click","clicking",
"clicks","client","clients","cliff","climate","climb","climbing","clinic",
"clinical","clinics","clinton","clip","clips","clock","clocks","clone",
"close","closed","closely","closer","closes","closest","closing","closure",
"cloth","clothes","clothing","cloud","clouds","cloudy","club","clubs",
"cluster","clusters","cnet","cnetcom","coach","coaches","coaching","coal",
"coalition","coast","coastal","coat","coated","coating","cock","cocks",
"code","codes","coding","coffee","cognitive","cohen","coin","coins",
"cold","cole","coleman","colin","collaboration","collaborative","collapse","collar",
"colleague","colleagues","collect","collectables","collected","collectible","collectibles","collecting",
"collection","collections","collective","collector","collectors","college","colleges","collins",
"cologne","colombia","colon","colonial","colony","color","colorado","colored",
"colors","colour","colours","columbia","columbus","column","columnists","columns",
"combat","combination","combinations","combine","combined","combines","combining","combo",
"come","comedy","comes","comfort","comfortable","comic","comics","coming",
"comm","command","commander","commands","comment","commentary","commented","comments",
"commerce","commercial","commission","commissioner","commissioners","commissions","commit","commitment",
"commitments","committed","committee","committees","commodities","commodity","common","commonly",
"commons","commonwealth","communicate","communication","communications","communist","communities","community",
"comp","compact","companies","companion","company","compaq","comparable","comparative",
"compare","compared","comparing","comparison","comparisons","compatibility","compatible","compensation",
"compete","competent","competing","competition","competitions","competitive","competitors","compilation",
"compile","compiled","compiler","complaint","complaints","complement","complete","completed",
"completely","completing","completion","complex","complexity","compliance","compliant","complicated",
"complications","complimentary","comply","component","components","composed","composer","composite",
"composition","compound","compounds","comprehensive","compressed","compression","compromise","computation",
"computational","compute","computed","computer","computers","computing","concentrate","concentration",
"concentrations","concept","concepts","conceptual","concern","concerned","concerning","concerns",
"concert","concerts","conclude","concluded","conclusion","conclusions","concord","concrete",
"condition","conditional","conditioning","conditions","condo","condos","conduct","conducted",
"conducting","conf","conference","conferences","conferencing","confidence","confident","confidential",
"confidentiality","config","configuration","configure","configured","configuring","confirm","confirmation",
"confirmed","conflict","conflicts","confused","confusion","congo","congratulations","congress",
"congressional","conjunction","connect","connected","connecticut","connecting","connection","connections",
"connectivity","connector","connectors","cons","conscious","consciousness","consecutive","consensus",
"consent","consequence","consequences","consequently","conservation","conservative","consider","considerable",
"consideration","considerations","considered","considering","considers","consist","consistency","consistent",
"consistently","consisting","consists","console","consoles","consolidated","consolidation","consortium",
"conspiracy","const","constant","constantly","constitute","constitutes","constitution","constitutional",
"constraint","constraints","construct","constructed","construction","consult","consultancy","consultant",
"consultants","consultation","consulting","consumer","consumers","consumption","contact","contacted",
"contacting","contacts","contain","contained","container","containers","containing","contains",
"contamination","contemporary","content","contents","contest","contests","context","continent",
"continental","continually","continue","continued","continues","continuing","continuity","continuous",
"continuously","contract","contracting","contractor","contractors","contracts","contrary","contrast",
"contribute","contributed","contributing","contribution","contributions","contributor","contributors","control",
"controlled","controller","controllers","controlling","controls","controversial","controversy","convenience",
"convenient","convention","conventional","conventions","convergence","conversation","conversations","conversion",
"convert","converted","converter","convertible","convicted","conviction","convinced","cook",
"cookbook","cooked","cookie","cookies","cooking","cool","cooler","cooling",
"cooper","cooperation","cooperative","coordinate","coordinated","coordinates","coordination","coordinator",
"cope","copied","copies","copper","copy","copying","copyright","copyrighted",
"copyrights","coral","cord","cordless","core","cork","corn","cornell",
"corner","corners","cornwall","corp","corporate","corporation","corporations","corps",
"corpus","correct","corrected","correction","corrections","correctly","correlation","correspondence",
"corresponding","corruption","cosmetic","cosmetics","cost","costa","costs","costume",
"costumes","cottage","cottages","cotton","could","council","councils","counsel",
"counseling","count","counted","counter","counters","counties","counting","countries",
"country","counts","county","couple","coupled","couples","coupon","coupons",
"courage","courier","course","courses","court","courtesy","courts","cove",
"cover","coverage","covered","covering","covers","cowboy","crack","cradle",
"craft","crafts","craig","crap","craps","crash","crawford","crazy",
"cream","create","created","creates","creating","creation","creations","creative",
"creativity","creator","creature","creatures","credit","credits","creek","crest",
"crew","cricket","crime","crimes","criminal","crisis","criteria","criterion",
"critical","criticism","critics","croatia","crop","crops","cross","crossing",
"crossword","crowd","crown","crucial","crude","cruise","cruises","cruz",
"crystal","cuba","cube","cubic","cuisine","cult","cultural","culture",
"cultures","cumshot","cumshots","cumulative","cups","cure","curious",
"currencies","currency","current","currently","curriculum","cursor","curtis","curve",
"curves","custody","custom","customer","customers","customise","customize","customized",
"customs","cute","cuts","cutting","cyber","cycle","cycles","cycling",
"cylinder","cyprus","czech","daddy","daily","dairy","daisy","dakota",
"dale","dallas","damage","damaged","damages","dame","damn","dana",
"dance","dancing","danger","dangerous","daniel","danish","danny","dans",
"dare","dark","darkness","darwin","dash","data","database","databases",
"date","dated","dates","dating","daughter","daughters","dave","david",
"davidson","davis","dawn","days","dayton","dead","deadline","deadly",
"deaf","deal","dealer","dealers","dealing","deals","dealt","dealtime",
"dean","dear","death","deaths","debate","debian","deborah","debt",
"debug","debut","decade","decades","december","decent","decide","decided",
"decimal","decision","decisions","deck","declaration","declare","declared","decline",
"declined","decor","decorating","decorative","decrease","decreased","dedicated","deemed",
"deep","deeper","deeply","deer","default","defeat","defects","defence",
"defend","defendant","defense","defensive","deferred","deficit","define","defined",
"defines","defining","definitely","definition","definitions","degree","degrees","delaware",
"delay","delayed","delays","delegation","delete","deleted","delhi","delicious",
"delight","deliver","delivered","delivering","delivers","delivery","dell","delta",
"deluxe","demand","demanding","demands","demo","democracy","democrat","democratic",
"democrats","demographic","demonstrate","demonstrated","demonstrates","demonstration","denial","denied",
"denmark","dennis","dense","density","dental","dentists","denver","deny",
"department","departmental","departments","departure","depend","dependence","dependent","depending",
"depends","deployment","deposit","deposits","depot","depression","dept","depth",
"deputy","derby","derek","derived","descending","describe","described","describes",
"describing","description","descriptions","desert","deserve","design","designated","designation",
"designed","designer","designers","designing","designs","desirable","desire","desired",
"desk","desktop","desktops","desperate","despite","destination","destinations","destiny",
"destroy","destroyed","destruction","detail","detailed","details","detect","detected",
"detection","detective","detector","determination","determine","determined","determines","determining",
"detroit","deutsch","deutsche","deutschland","devel","develop","developed","developer",
"developers","developing","development","developmental","developments","develops","deviant","deviation",
"device","devices","devil","devon","devoted","diabetes","diagnosis","diagnostic",
"diagram","dial","dialog","dialogue","diameter","diamond","diamonds","diana",
"diane","diary","dice","dicke","dictionaries","dictionary",
"died","diego","dies","diesel","diet","dietary","diff","differ",
"difference","differences","different","differential","differently","difficult","difficulties","difficulty",
"diffs","digest","digit","digital","dimension","dimensional",
"dimensions","dining","dinner","diploma","direct","directed","direction","directions",
"directive","directly","director","directories","directors","directory","dirt","dirty",
"disabilities","disability","disable","disabled","disagree","disappointed","disaster","disc",
"discharge","disciplinary","discipline","disciplines","disclaimer","disclaimers","disclose","disclosure",
"disco","discount","discounted","discounts","discover","discovered","discovery","discrete",
"discretion","discrimination","discs","discuss","discussed","discusses","discussing","discussion",
"discussions","disease","diseases","dish","dishes","disk","disks","disney",
"disorder","disorders","dispatch","dispatched","display","displayed","displaying","displays",
"disposal","disposition","dispute","disputes","dist","distance","distances","distant",
"distinct","distinction","distinguished","distribute","distributed","distribution","distributions","distributor",
"distributors","district","districts","disturbed","dive","diverse","diversity","divide",
"divided","dividend","divine","diving","division","divisions","divorce","divx",
"dock","docs","doctor","doctors","doctrine","document","documentary","documentation",
"documentcreatetextnode","documented","documents","dodge","does","dogs","doing","doll",
"dollar","dollars","dolls","domain","domains","dome","domestic","dominant",
"dominican","donald","donate","donated","donation","donations","done","donna",
"donor","donors","dont","doom","door","doors","dosage","dose",
"double","doubt","doug","douglas","dover","down","download","downloadable",
"downloadcom","downloaded","downloading","downloads","downtown","dozen","dozens","draft",
"drag","dragon","drain","drainage","drama","dramatic","dramatically","draw",
"drawing","drawings","drawn","draws","dream","dreams","dress","dressed",
"dresses","dressing","drew","dried","drill","drilling","drink","drinking",
"drinks","drive","driven","driver","drivers","drives","driving","drop",
"dropped","drops","drove","drug","drugs","drum","drums","drunk",
"dryer","dual","dubai","dublin","duck","dude","duke","dumb",
"dump","duncan","duplicate","durable","duration","durham","during","dust",
"dutch","duties","duty","dvds","dying","dylan","dynamic","dynamics",
"each","eagle","eagles","earl","earlier","earliest","early","earn",
"earned","earning","earnings","earrings","ears","earth","earthquake","ease",
"easier","easily","east","easter","eastern","easy","eating","ebay",
"ebony","ebook","ebooks","echo","eclipse","ecological","ecology","ecommerce",
"economic","economics","economies","economy","ecuador","eddie","eden","edgar",
"edge","edges","edinburgh","edit","edited","editing","edition","editions",
"editor","editorial","editorials","editors","edmonton","educated","education","educational",
"educators","edward","edwards","effect","effective","effectively","effectiveness","effects",
"efficiency","efficient","efficiently","effort","efforts","eggs","egypt","egyptian",
"eight","either","ejaculation","elder","elderly","elect","elected","election",
"elections","electoral","electric","electrical","electricity","electro","electron","electronic",
"electronics","elegant","element","elementary","elements","elephant","elevation","eleven",
"eligibility","eligible","eliminate","elimination","elite","elizabeth","ellen","elliott",
"ellis","else","elsewhere","elvis","emacs","email","emails","embassy",
"embedded","emerald","emergency","emerging","emily","eminem","emirates","emission",
"emissions","emma","emotional","emotions","emperor","emphasis","empire","empirical",
"employ","employed","employee","employees","employer","employers","employment","empty",
"enable","enabled","enables","enabling","enclosed","enclosure","encoding","encounter",
"encountered","encourage","encouraged","encourages","encouraging","encryption","encyclopedia","endangered",
"ended","endif","ending","endless","endorsed","endorsement","ends","enemies",
"enemy","energy","enforcement","engage","engaged","engagement","engaging","engine",
"engineer","engineering","engineers","engines","england","english","enhance","enhanced",
"enhancement","enhancements","enhancing","enjoy","enjoyed","enjoying","enlarge","enlargement",
"enormous","enough","enquiries","enquiry","enrolled","enrollment","ensemble","ensure",
"ensures","ensuring","enter","entered","entering","enterprise","enterprises","enters",
"entertaining","entertainment","entire","entirely","entities","entitled","entity","entrance",
"entrepreneur","entrepreneurs","entries","entry","envelope","environment","environmental","environments",
"enzyme","epic","epinions","epinionscom","episode","episodes","epson","equal",
"equality","equally","equation","equations","equilibrium","equipment","equipped","equity",
"equivalent","eric","ericsson","erik","erotic","erotica","error","errors",
"escape","escort","escorts","especially","espn","essay","essays","essence",
"essential","essentially","essentials","essex","establish","established","establishing","establishment",
"estate","estates","estimate","estimated","estimates","estimation","estonia","eternal",
"ethernet","ethical","ethics","ethiopia","ethnic","eugene","euro","europe",
"european","euros","eval","evaluate","evaluated","evaluating","evaluation","evaluations",
"evanescence","evans","even","evening","event","events","eventually","ever",
"every","everybody","everyday","everyone","everything","everywhere","evidence","evident",
"evil","evolution","exact","exactly","exam","examination","examinations","examine",
"examined","examines","examining","example","examples","exams","exceed","excel",
"excellence","excellent","except","exception","exceptional","exceptions","excerpt","excess",
"excessive","exchange","exchanges","excited","excitement","exciting","exclude","excluded",
"excluding","exclusion","exclusive","exclusively","excuse","exec","execute","executed",
"execution","executive","executives","exempt","exemption","exercise","exercises","exhaust",
"exhibit","exhibition","exhibitions","exhibits","exist","existed","existence","existing",
"exists","exit","exotic","expand","expanded","expanding","expansion","expansys",
"expect","expectations","expected","expects","expedia","expenditure","expenditures","expense",
"expenses","expensive","experience","experienced","experiences","experiencing","experiment","experimental",
"experiments","expert","expertise","experts","expiration","expired","expires","explain",
"explained","explaining","explains","explanation","explicit","explicitly","exploration","explore",
"explorer","exploring","explosion","expo","export","exports","exposed","exposure",
"express","expressed","expression","expressions","extend","extended","extending","extends",
"extension","extensions","extensive","extent","exterior","external","extra","extract",
"extraction","extraordinary","extras","extreme","extremely","eyed","eyes","fabric",
"fabrics","fabulous","face","faced","faces","facial","facilitate","facilities",
"facility","facing","fact","factor","factors","factory","facts","faculty",
"fail","failed","failing","fails","failure","failures","fair","fairfield",
"fairly","fairy","faith","fake","fall","fallen","falling","falls",
"false","fame","familiar","families","family","famous","fancy","fans",
"fantastic","fantasy","faqs","fare","fares","farm","farmer","farmers",
"farming","farms","fascinating","fashion","fast","faster","fastest","fatal",
"fate","father","fathers","fatty","fault","favor","favorite","favorites",
"favors","favour","favourite","favourites","fear","fears","feat","feature",
"featured","features","featuring","february","federal","federation","feed","feedback",
"feeding","feeds","feel","feeling","feelings","feels","fees","feet",
"fell","fellow","fellowship","felt","female","females","fence","feof",
"ferrari","ferry","festival","festivals","fetish","fever","fewer","fiber",
"fibre","fiction","field","fields","fifteen","fifth","fifty","fight",
"fighter","fighters","fighting","figure","figured","figures","fiji","file",
"filed","filename","files","filing","fill","filled","filling","film",
"filme","films","filter","filtering","filters","final","finally","finals",
"finance","finances","financial","financing","find","findarticles","finder","finding",
"findings","findlaw","finds","fine","finest","finger","fingering","fingers",
"finish","finished","finishing","finite","finland","finnish","fioricet","fire",
"fired","firefox","fireplace","fires","firewall","firewire","firm","firms",
"firmware","first","fiscal","fish","fisher","fisheries","fishing","fist",
"fisting","fitness","fits","fitted","fitting","five","fixed","fixes",
"fixtures","flag","flags","flame","flash","flashers","flashing","flat",
"flavor","fleece","fleet","flesh","flex","flexibility","flexible","flickr",
"flight","flights","flip","float","floating","flood","floor","flooring",
"floors","floppy","floral","florence","florida","florist","florists","flour",
"flow","flower","flowers","flows","floyd","fluid","flush","flux",
"flyer","flying","foam","focal","focus","focused","focuses","focusing",
"fold","folder","folders","folding","folk","folks","follow","followed",
"following","follows","font","fonts","food","foods","fool","foot",
"footage","football","footwear","forbes","forbidden","force","forced","forces",
"ford","forecast","forecasts","foreign","forest","forestry","forests","forever",
"forge","forget","forgot","forgotten","fork","form","formal","format",
"formation","formats","formatting","formed","former","formerly","forming","forms",
"formula","fort","forth","fortune","forty","forum","forums","forward",
"forwarding","fossil","foster","foto","fotos","fought","foul","found",
"foundation","foundations","founded","founder","fountain","four","fourth","fraction",
"fragrance","fragrances","frame","framed","frames","framework","framing","france",
"franchise","francis","francisco","frank","frankfurt","franklin","fraser","fraud",
"fred","frederick","free","freebsd","freedom","freelance","freely","freeware",
"freeze","freight","french","frequencies","frequency","frequent","frequently","fresh",
"friday","fridge","friend","friendly","friends","friendship","frog","from",
"front","frontier","frontpage","frost","frozen","fruit","fruits","fuel","fuji","fujitsu","full","fully","function",
"functional","functionality","functioning","functions","fund","fundamental","fundamentals","funded",
"funding","fundraising","funds","funeral","funk","funky","funny","furnished",
"furnishings","furniture","further","furthermore","fusion","future","futures","fuzzy",
"gabriel","gadgets","gage","gain","gained","gains","galaxy","gale",
"galleries","gallery","gambling","game","gamecube","games","gamespot","gaming",
"gamma","gang","gangbang","gaps","garage","garbage","garcia","garden",
"gardening","gardens","garlic","garmin","gary","gasoline","gate","gates",
"gateway","gather","gathered","gathering","gauge","gave","gays","gazette",
"gear","geek","gender","gene","genealogy","general","generally","generate",
"generated","generates","generating","generation","generations","generator","generators","generic",
"generous","genes","genesis","genetic","genetics","geneva","genius","genome",
"genre","genres","gentle","gentleman","gently","genuine","geographic","geographical",
"geography","geological","geology","geometry","george","georgia","gerald","german",
"germany","gets","getting","ghana","ghost","giant","giants","gibraltar",
"gibson","gift","gifts","gilbert","girl","girlfriend","girls","give",
"given","gives","giving","glad","glance","glasgow","glass","glasses",
"glen","glenn","global","globe","glory","glossary","gloves","glow",
"glucose","gmbh","gnome","goal","goals","goat","gods","goes",
"going","gold","golden","golf","gone","gonna","good","goods",
"google","gordon","gore","gorgeous","gospel","gossip","gothic","goto",
"gotta","gotten","gourmet","governance","governing","government","governmental","governments",
"governor","govt","grab","grace","grad","grade","grades","gradually",
"graduate","graduated","graduates","graduation","graham","grain","grammar","grams",
"grand","grande","granny","grant","granted","grants","graph","graphic",
"graphical","graphics","graphs","gras","grass","grateful","gratis","gratuit",
"grave","gravity","gray","great","greater","greatest","greatly","greece",
"greek","green","greene","greenhouse","greensboro","greeting","greetings","greg",
"gregory","grenada","grew","grey","grid","griffin","grill","grip",
"grocery","groove","gross","ground","grounds","groundwater","group","groups",
"grove","grow","growing","grown","grows","growth","guam","guarantee",
"guaranteed","guarantees","guard","guardian","guards","guatemala","guess","guest",
"guestbook","guests","guidance","guide","guided","guidelines","guides","guild",
"guilty","guinea","guitar","guitars","gulf","guns","guru","guyana",
"guys","gzip","habitat","habits","hack","hacker","hair","hairy",
"haiti","half","halfcom","halifax","hall","halloween","halo","hamburg",
"hamilton","hammer","hampshire","hampton","hand","handbags","handbook","handed",
"handheld","handhelds","handjob","handjobs","handle","handled","handles","handling",
"handmade","hands","handy","hang","hanging","hans","hansen","happen",
"happened","happening","happens","happiness","happy","harassment","harbor","harbour",
"hard","hardcore","hardcover","harder","hardly","hardware","hardwood","harley",
"harm","harmful","harmony","harold","harper","harris","harrison","harry",
"hart","hartford","harvard","harvest","harvey","hash","hate","hats",
"have","haven","having","hawaii","hawaiian","hawk","hayes","hazard",
"hazardous","hazards","hdtv","head","headed","header","headers","heading",
"headline","headlines","headphones","headquarters","heads","headset","healing","health",
"healthcare","healthy","hear","heard","hearing","hearings","heart","hearts",
"heat","heated","heater","heath","heather","heating","heaven","heavily",
"heavy","hebrew","heel","height","heights","held","helen","helena",
"helicopter","hell","hello","helmet","help","helped","helpful","helping",
"helps","hence","henderson","henry","hentai","hepatitis","herald","herb",
"herbal","herbs","here","hereby","herein","heritage","hero","heroes",
"herself","hewlett","hidden","hide","hierarchy","high","higher","highest",
"highland","highlight","highlighted","highlights","highly","highs","highway","highways",
"hiking","hill","hills","hilton","himself","hindu","hint","hints",
"hire","hired","hiring","hispanic","hist","historic","historical","history",
"hitachi","hits","hitting","hobbies","hobby","hockey","hold","holdem",
"holder","holders","holding","holdings","holds","hole","holes","holiday",
"holidays","holland","hollow","holly","hollywood","holmes","holocaust","holy",
"home","homeland","homeless","homepage","homes","hometown","homework","honda",
"honduras","honest","honey","hong","honolulu","honor","honors","hood",
"hook","hope","hoped","hopefully","hopes","hoping","hopkins","horizon",
"horizontal","hormone","horn","horny","horrible","horror","horse","horses",
"hose","hospital","hospitality","hospitals","host","hosted","hostel","hostels",
"hosting","hosts","hotel","hotels","hotelscom","hotmail","hottest","hour",
"hourly","hours","house","household","households","houses","housewares","housewives",
"housing","houston","howard","however","howto","href","html","http",
"hudson","huge","hugh","hughes","hugo","hull","human","humanitarian",
"humanities","humanity","humans","humidity","humor","hundred","hundreds","hung",
"hungarian","hungary","hunger","hungry","hunt","hunter","hunting","huntington",
"hurricane","hurt","husband","hybrid","hydraulic","hydrocodone","hydrogen","hygiene",
"hypothesis","hypothetical","hyundai","iceland","icon","icons","idaho","idea",
"ideal","ideas","identical","identification","identified","identifier","identifies","identify",
"identifying","identity","idle","idol","ieee","ignore","ignored","illegal",
"illinois","illness","illustrated","illustration","illustrations","image","images","imagination",
"imagine","imaging","immediate","immediately","immigrants","immigration","immune","immunology",
"impact","impacts","impaired","imperial","implement","implementation","implemented","implementing",
"implications","implied","implies","import","importance","important","importantly","imported",
"imports","impose","imposed","impossible","impressed","impression","impressive","improve",
"improved","improvement","improvements","improving","inappropriate","inbox","incentive","incentives",
"incest","inch","inches","incidence","incident","incidents","incl","include",
"included","includes","including","inclusion","inclusive","income","incoming","incomplete",
"incorporate","incorporated","incorrect","increase","increased","increases","increasing","increasingly",
"incredible","incurred","indeed","independence","independent","independently","index","indexed",
"indexes","india","indian","indiana","indianapolis","indians","indicate","indicated",
"indicates","indicating","indication","indicator","indicators","indices","indie","indigenous",
"indirect","individual","individually","individuals","indonesia","indonesian","indoor","induced",
"induction","industrial","industries","industry","inexpensive","infant","infants","infected",
"infection","infections","infectious","infinite","inflation","influence","influenced","influences",
"info","inform","informal","information","informational","informative","informed","infrared",
"infrastructure","ingredients","inherited","initial","initially","initiated","initiative","initiatives",
"injection","injured","injuries","injury","inkjet","inline","inner","innocent",
"innovation","innovations","innovative","inns","input","inputs","inquire","inquiries",
"inquiry","insects","insert","inserted","insertion","inside","insider","insight",
"insights","inspection","inspections","inspector","inspiration","inspired","install","installation",
"installations","installed","installing","instance","instances","instant","instantly","instead",
"institute","institutes","institution","institutional","institutions","instruction","instructional","instructions",
"instructor","instructors","instrument","instrumental","instrumentation","instruments","insulin","insurance",
"insured","intake","integer","integral","integrate","integrated","integrating","integration",
"integrity","intel","intellectual","intelligence","intelligent","intend","intended","intense",
"intensity","intensive","intent","intention","inter","interact","interaction","interactions",
"interactive","interest","interested","interesting","interests","interface","interfaces","interference",
"interim","interior","intermediate","internal","international","internationally","internet","internship",
"interpretation","interpreted","interracial","intersection","interstate","interval","intervals","intervention",
"interventions","interview","interviews","intimate","intl","into","intranet","intro",
"introduce","introduced","introduces","introducing","introduction","introductory","invalid","invasion",
"invention","inventory","invest","investigate","investigated","investigation","investigations","investigator",
"investigators","investing","investment","investments","investor","investors","invisible","invision",
"invitation","invitations","invite","invited","invoice","involve","involved","involvement",
"involves","involving","iowa","ipaq","ipod","iran","iraq","iraqi",
"ireland","irish","iron","irrigation","isaac","isbn","islam","islamic",
"island","islands","isle","isolated","isolation","israel","israeli","issn",
"issue","issued","issues","istanbul","italia","italian","italiano","italic",
"italy","item","items","itsa","itself","itunes","ivory","jack",
"jacket","jackets","jackie","jackson","jacksonville","jacob","jade","jaguar",
"jail","jake","jamaica","james","jamie","jane","janet","january",
"japan","japanese","jason","java","javascript","jazz","jean","jeans",
"jeep","jeff","jefferson","jeffrey","jelsoft","jennifer","jenny","jeremy",
"jerry","jersey","jerusalem","jesse","jessica","jesus","jets","jewel",
"jewellery","jewelry","jewish","jews","jill","jimmy","joan","jobs",
"joel","john","johnny","johns","johnson","johnston","join","joined",
"joining","joins","joint","joke","jokes","jonathan","jones","jordan",
"jose","joseph","josh","joshua","journal","journalism","journalist","journalists",
"journals","journey","joyce","jpeg","juan","judge","judges","judgment",
"judicial","judy","juice","julia","julian","julie","july","jump",
"jumping","junction","june","jungle","junior","junk","jurisdiction","jury",
"just","justice","justify","justin","juvenile","kansas","karaoke","karen",
"karl","karma","kate","kathy","katie","katrina","kazakhstan","keen",
"keep","keeping","keeps","keith","kelkoo","kelly","kennedy","kenneth",
"kenny","keno","kent","kentucky","kenya","kept","kernel","kerry",
"kevin","keyboard","keyboards","keys","keyword","keywords","kick","kidney",
"kids","kijiji","kill","killed","killer","killing","kills","kilometers",
"kinase","kind","kinda","kinds","king","kingdom","kings","kingston",
"kirk","kiss","kissing","kitchen","kits","kitty","klein","knee",
"knew","knife","knight","knights","knit","knitting","knives","knock",
"know","knowing","knowledge","knowledgestorm","known","knows","kodak","kong",
"korea","korean","kruger","kurt","kuwait","kyle","label","labeled",
"labels","labor","laboratories","laboratory","labour","labs","lace","lack",
"ladder","laden","ladies","lady","lafayette","laid","lake","lakes",
"lamb","lambda","lamp","lamps","lancaster","lance","land","landing",
"lands","landscape","landscapes","lane","lanes","lang","language","languages",
"lanka","laptop","laptops","large","largely","larger","largest","larry",
"laser","last","lasting","late","lately","later","latest","latex",
"latin","latina","latinas","latino","latitude","latter","latvia","lauderdale",
"laugh","laughing","launch","launched","launches","laundry","laura","lauren",
"lawn","lawrence","laws","lawsuit","lawyer","lawyers","layer","layers",
"layout","lazy","lead","leader","leaders","leadership","leading","leads",
"leaf","league","lean","learn","learned","learners","learning","lease",
"leasing","least","leather","leave","leaves","leaving","lebanon","lecture",
"lectures","leeds","left","legacy","legal","legally","legend","legendary",
"legends","legislation","legislative","legislature","legitimate","legs","leisure","lemon",
"lender","lenders","lending","length","lens","lenses","leon","leonard",
"leone","lesbian","lesbians","leslie","less","lesser","lesson","lessons",
"lets","letter","letters","letting","level","levels","levitra","levy",
"lewis","lexington","lexmark","lexus","liabilities","liability","liable","liberal",
"liberia","liberty","librarian","libraries","library","libs","licence","license",
"licensed","licenses","licensing","licking","liechtenstein","lies","life","lifestyle",
"lifetime","lift","light","lighter","lighting","lightning","lights","lightweight",
"like","liked","likelihood","likely","likes","likewise","lime","limit",
"limitation","limitations","limited","limiting","limits","limousines","lincoln","linda",
"lindsay","line","linear","lined","lines","lingerie","link","linked",
"linking","links","linux","lion","lions","lips","liquid","lisa",
"list","listed","listen","listening","listing","listings","listprice","lists",
"lite","literacy","literally","literary","literature","lithuania","litigation","little",
"live","livecam","lived","liver","liverpool","lives","livesex","livestock",
"living","lloyd","load","loaded","loading","loads","loan","loans",
"lobby","local","locale","locally","locate","located","location","locations",
"locator","lock","locked","locking","locks","lodge","lodging","logan",
"logged","logging","logic","logical","login","logistics","logitech","logo",
"logos","logs","lolita","london","lone","lonely","long","longer",
"longest","longitude","look","looked","looking","looks","looksmart","lookup",
"loop","loops","loose","lopez","lord","lose","losing","loss",
"losses","lost","lots","lottery","lotus","loud","louis","louise",
"louisiana","louisville","lounge","love","loved","lovely","lover","lovers",
"loves","loving","lower","lowest","lows","lucas","lucia","luck",
"lucky","lucy","luggage","luis","luke","lunch","lung","luther",
"luxembourg","luxury","lycos","lying","lynn","lyric","lyrics","macedonia",
"machine","machinery","machines","macintosh","macro","macromedia","madagascar","made",
"madison","madness","madonna","madrid","magazine","magazines","magic","magical",
"magnet","magnetic","magnificent","magnitude","maiden","mail","mailed","mailing",
"mailman","mails","mailto","main","maine","mainland","mainly","mainstream",
"maintain","maintained","maintaining","maintains","maintenance","major","majority","make",
"maker","makers","makes","makeup","making","malawi","malaysia","maldives",
"male","males","mali","mall","malpractice","malta","mambo","manage",
"managed","management","manager","managers","managing","manchester","mandate","mandatory",
"manga","manhattan","manitoba","manner","manor","manual","manually","manuals",
"manufacture","manufactured","manufacturer","manufacturers","manufacturing","many","maple","mapping",
"maps","marathon","marble","marc","march","marco","marcus","mardi",
"margaret","margin","maria","mariah","marie","marijuana","marilyn","marina",
"marine","mario","marion","maritime","mark","marked","marker","markers",
"market","marketing","marketplace","markets","marking","marks","marriage","married",
"marriott","mars","marshall","mart","martha","martial","martin","marvel",
"mary","maryland","mask","mason","mass","massachusetts","massage","massive",
"master","mastercard","masters","masturbating","masturbation","match","matched","matches",
"matching","mate","material","materials","maternity","math","mathematical","mathematics",
"mating","matrix","mats","matt","matter","matters","matthew","mattress",
"mature","maui","mauritius","maximize","maximum","maybe","mayor","mazda",
"mcdonald","meal","meals","mean","meaning","meaningful","means","meant",
"meanwhile","measure","measured","measurement","measurements","measures","measuring","meat",
"mechanical","mechanics","mechanism","mechanisms","medal","media","median","medicaid",
"medical","medicare","medication","medications","medicine","medicines","medieval","meditation",
"mediterranean","medium","medline","meet","meeting","meetings","meets","meetup",
"mega","melbourne","melissa","member","members","membership","membrane","memo",
"memorabilia","memorial","memories","memory","memphis","mens","ment","mental",
"mention","mentioned","mentor","menu","menus","mercedes","merchandise","merchant",
"merchants","mercury","mercy","mere","merely","merge","merger","merit",
"merry","mesa","mesh","mess","message","messages","messaging","messenger",
"meta","metabolism","metadata","metal","metallic","metallica","metals","meter",
"meters","method","methodology","methods","metres","metric","metro","metropolitan",
"mexican","mexico","meyer","miami","mice","michael","michel","michelle",
"michigan","micro","microphone","microsoft","microwave","middle","midi","midlands",
"midnight","midwest","might","mighty","migration","mike","milan","mild",
"mile","mileage","miles","milf","milfhunter","milfs","military","milk",
"mill","millennium","miller","million","millions","mills","milton","milwaukee",
"mime","mind","minds","mine","mineral","minerals","mines","mini",
"miniature","minimal","minimize","minimum","mining","minister","ministers","ministries",
"ministry","minneapolis","minnesota","minolta","minor","minority","mins","mint",
"minus","minute","minutes","miracle","mirror","mirrors","misc","miscellaneous",
"miss","missed","missile","missing","mission","missions","mississippi","missouri",
"mistake","mistakes","mistress","mitchell","mitsubishi","mixed","mixer","mixing",
"mixture","mobile","mobiles","mobility","mode","model","modeling","modelling",
"models","modem","modems","moderate","moderator","moderators","modern","modes",
"modification","modifications","modified","modify","mods","modular","module","modules",
"moisture","mold","moldova","molecular","molecules","moment","moments","momentum",
"moms","monaco","monday","monetary","money","mongolia","monica","monitor",
"monitored","monitoring","monitors","monkey","mono","monroe","monster","montana",
"monte","montgomery","month","monthly","months","montreal","mood","moon",
"moore","moral","more","moreover","morgan","morning","morocco","morris",
"morrison","mortality","mortgage","mortgages","moscow","moses","moss","most",
"mostly","motel","motels","mother","motherboard","mothers","motion","motivated",
"motivation","motor","motorcycle","motorcycles","motorola","motors","mount","mountain",
"mountains","mounted","mounting","mounts","mouse","mouth","move","moved",
"movement","movements","movers","moves","movie","movies","moving","mozambique",
"mozilla","mpeg","mpegs","mrna","msgid","msgstr","msie","much",
"multi","multimedia","multiple","mumbai","munich","municipal","municipality","murder",
"murphy","murray","muscle","muscles","museum","museums","music","musical",
"musician","musicians","muslim","muslims","must","mustang","mutual","muze",
"myanmar","myers","myrtle","myself","mysimon","myspace","mysql","mysterious",
"mystery","myth","nail","nails","naked","name","named","namely",
"names","namespace","namibia","nancy","nano","naples","narrative","narrow",
"nasa","nascar","nasdaq","nashville","nasty","nathan","nation","national",
"nationally","nations","nationwide","native","nato","natural","naturally","naturals",
"nature","naughty","naval","navigate","navigation","navigator","navy","ncaa",
"near","nearby","nearest","nearly","nebraska","necessarily","necessary","necessity",
"neck","necklace","need","needed","needle","needs","negative","negotiation",
"negotiations","neighbor","neighborhood","neighbors","neil","neither","nelson","neon",
"nepal","nerve","nervous","nest","nested","netherlands","netscape","network",
"networking","networks","neural","neutral","nevada","never","nevertheless","newark",
"newbie","newcastle","newer","newest","newfoundland","newly","newport","news",
"newscom","newsletter","newsletters","newspaper","newspapers","newton","next","nextel",
"niagara","nicaragua","nice","nicholas","nick","nickel","nickname","nicole",
"niger","nigeria","night","nightlife","nightmare","nights","nike","nikon",
"nine","nintendo","nipple","nipples","nirvana","nissan","nitrogen","noble",
"nobody","node","nodes","noise","nokia","nominated","nomination","nominations",
"none","nonprofit","noon","norfolk","norm","normal","normally","norman",
"north","northeast","northern","northwest","norton","norway","norwegian","nose",
"note","notebook","notebooks","noted","notes","nothing","notice","noticed",
"notices","notification","notifications","notified","notify","notion","notre","nottingham",
"nova","novel","novels","novelty","november","nowhere","ntsc","nuclear",
"nude","nudist","nudity","nuke","null","number","numbers","numeric",
"numerical","numerous","nurse","nursery","nurses","nursing","nutrition","nutritional",
"nuts","nutten","nvidia","nylon","oakland","oaks","oasis","obesity",
"obituaries","object","objective","objectives","objects","obligation","obligations","observation",
"observations","observe","observed","observer","obtain","obtained","obtaining","obvious",
"obviously","occasion","occasional","occasionally","occasions","occupation","occupational","occupations",
"occupied","occur","occurred","occurrence","occurring","occurs","ocean","oclc",
"october","odds","oecd","offense","offensive","offer","offered","offering",
"offerings","offers","office","officer","officers","offices","official","officially",
"officials","offline","offset","offshore","often","ohio","oils","okay",
"oklahoma","older","oldest","olive","oliver","olympic","olympics","olympus",
"omaha","oman","omega","omissions","once","ones","ongoing","onion",
"online","only","ontario","onto","oops","open","opened","opening",
"openings","opens","opera","operate","operated","operates","operating","operation",
"operational","operations","operator","operators","opinion","opinions","opponent","opponents",
"opportunities","opportunity","opposed","opposite","opposition","optical","optics","optimal",
"optimization","optimize","optimum","option","optional","options","oracle","oral",
"orange","orbit","orchestra","order","ordered","ordering","orders","ordinance",
"ordinary","oregon","organ","organic","organisation","organisations","organised","organisms",
"organization","organizational","organizations","organize","organized","organizer","organizing","orgasm",
"orgy","oriental","orientation","oriented","origin","original","originally","origins",
"orlando","orleans","oscar","other","others","otherwise","ottawa","ought",
"ours","ourselves","outcome","outcomes","outdoor","outdoors","outer","outlet",
"outline","outlined","outlook","output","outputs","outreach","outside","outsourcing",
"outstanding","oval","oven","over","overall","overcome","overhead","overnight",
"overseas","overview","owen","owned","owner","owners","ownership","owns",
"oxford","oxide","oxygen","ozone","pace","pacific","pack","package",
"packages","packaging","packard","packed","packet","packets","packing","packs",
"pads","page","pages","paid","pain","painful","paint","paintball",
"painted","painting","paintings","pair","pairs","pakistan","palace","pale",
"palestine","palestinian","palm","palmer","pamela","panama","panasonic","panel",
"panels","panic","panties","pants","pantyhose","paper","paperback","paperbacks",
"papers","papua","para","parade","paradise","paragraph","paragraphs","paraguay",
"parallel","parameter","parameters","parcel","parent","parental","parenting","parents",
"paris","parish","park","parker","parking","parks","parliament","parliamentary",
"part","partial","partially","participant","participants","participate","participated","participating",
"participation","particle","particles","particular","particularly","parties","partition","partly",
"partner","partners","partnership","partnerships","parts","party","paso","pass",
"passage","passed","passenger","passengers","passes","passing","passion","passive",
"passport","password","passwords","past","pasta","paste","pastor","patch",
"patches","patent","patents","path","pathology","paths","patient","patients",
"patio","patricia","patrick","patrol","pattern","patterns","paul","pavilion",
"paxil","payable","payday","paying","payment","payments","paypal","payroll",
"pays","pdas","peace","peaceful","peak","pearl","peas","pediatric",
"peeing","peer","peers","penalties","penalty","pencil","pendant","pending",
"penetration","penguin","peninsula","penn","pennsylvania","penny","pens",
"pension","pensions","pentium","people","peoples","pepper","perceived","percent",
"percentage","perception","perfect","perfectly","perform","performance","performances","performed",
"performer","performing","performs","perfume","perhaps","period","periodic","periodically",
"periods","peripheral","peripherals","perl","permalink","permanent","permission","permissions",
"permit","permits","permitted","perry","persian","persistent","person","personal",
"personality","personalized","personally","personals","personnel","persons","perspective","perspectives",
"perth","peru","pest","pete","peter","petersburg","peterson","petite",
"petition","petroleum","pets","phantom","pharmaceutical","pharmaceuticals","pharmacies","pharmacology",
"pharmacy","phase","phases","phenomenon","phentermine","phil","philadelphia","philip",
"philippines","philips","phillips","philosophy","phoenix","phone","phones","photo",
"photograph","photographer","photographers","photographic","photographs","photography","photos","photoshop",
"phpbb","phrase","phrases","phys","physical","physically","physician","physicians",
"physics","physiology","piano","pichunter","pick","picked","picking","picks",
"pickup","picnic","pics","picture","pictures","piece","pieces","pierce",
"pierre","pike","pill","pillow","pills","pilot","pine","ping",
"pink","pins","pioneer","pipe","pipeline","pipes","pirates",
"pitch","pittsburgh","pixel","pixels","pizza","place","placed",
"placement","places","placing","plain","plains","plaintiff","plan","plane",
"planes","planet","planets","planned","planner","planners","planning","plans",
"plant","plants","plasma","plastic","plastics","plate","plates","platform",
"platforms","platinum","play","playback","playboy","played","player","players",
"playing","playlist","plays","playstation","plaza","pleasant","please","pleased",
"pleasure","pledge","plenty","plot","plots","plug","plugin","plugins",
"plumbing","plus","plymouth","pmid","pocket","pockets","podcast","podcasts",
"poem","poems","poet","poetry","point","pointed","pointer","pointing",
"points","pokemon","poker","poland","polar","pole","police","policies",
"policy","polish","polished","political","politicians","politics","poll","polls",
"pollution","polo","poly","polyester","polymer","polyphonic","pond","pontiac",
"pool","pools","poor","pope","popular","popularity","population","populations",
"porcelain","pork","porn","porno","porsche","port","portable","portal",
"porter","portfolio","portion","portions","portland","portrait","portraits","ports",
"portsmouth","portugal","portuguese","pose","posing","position","positioning","positions",
"positive","possess","possession","possibilities","possibility","possible","possibly","post",
"postage","postal","postcard","postcards","posted","poster","posters","posting",
"postings","postposted","posts","potato","potatoes","potential","potentially","potter",
"pottery","poultry","pound","pounds","pour","poverty","powder","powell",
"power","powered","powerful","powerpoint","powers","powerseller","practical","practice",
"practices","practitioner","practitioners","prague","prairie","praise","pray","prayer",
"prayers","preceding","precious","precipitation","precise","precisely","precision","predict",
"predicted","prediction","predictions","prefer","preference","preferences","preferred","prefers",
"prefix","pregnancy","pregnant","preliminary","premier","premiere","premises","premium",
"prep","prepaid","preparation","prepare","prepared","preparing","prerequisite","prescribed",
"prescription","presence","present","presentation","presentations","presented","presenting","presently",
"presents","preservation","preserve","president","presidential","press","pressed","pressing",
"pressure","preston","pretty","prev","prevent","preventing","prevention","preview",
"previews","previous","previously","price","priced","prices","pricing","pride",
"priest","primarily","primary","prime","prince","princess","princeton","principal",
"principle","principles","print","printable","printed","printer","printers","printing",
"prints","prior","priorities","priority","prison","prisoner","prisoners","privacy",
"private","privilege","privileges","prix","prize","prizes","probability","probably",
"probe","problem","problems","proc","procedure","procedures","proceed","proceeding",
"proceedings","proceeds","process","processed","processes","processing","processor","processors",
"procurement","produce","produced","producer","producers","produces","producing","product",
"production","productions","productive","productivity","products","prof","profession","professional",
"professionals","professor","profile","profiles","profit","profits","program","programme",
"programmer","programmers","programmes","programming","programs","progress","progressive","prohibited",
"project","projected","projection","projector","projectors","projects","prominent","promise",
"promised","promises","promising","promo","promote","promoted","promotes","promoting",
"promotion","promotional","promotions","prompt","promptly","proof","propecia","proper",
"properly","properties","property","prophet","proportion","proposal","proposals","propose",
"proposed","proposition","proprietary","pros","prospect","prospective","prospects","prostate",
"prostores","prot","protect","protected","protecting","protection","protective","protein",
"proteins","protest","protocol","protocols","prototype","proud","proudly","prove",
"proved","proven","provide","provided","providence","provider","providers","provides",
"providing","province","provinces","provincial","provision","provisions","proxy","prozac",
"psychiatry","psychological","psychology","public","publication","publications","publicity","publicly",
"publish","published","publisher","publishers","publishing","pubmed","pubs","puerto",
"pull","pulled","pulling","pulse","pump","pumps","punch","punishment",
"punk","pupils","puppy","purchase","purchased","purchases","purchasing","pure",
"purple","purpose","purposes","purse","pursuant","pursue","pursuit","push",
"pushed","pushing","puts","putting","puzzle","puzzles","python",
"qatar","quad","qualification","qualifications","qualified","qualify","qualifying","qualities",
"quality","quantitative","quantities","quantity","quantum","quarter","quarterly","quarters",
"quebec","queen","queens","queensland","queries","query","quest","question",
"questionnaire","questions","queue","quick","quickly","quiet","quilt","quit",
"quite","quiz","quizzes","quotations","quote","quoted","quotes","rabbit",
"race","races","rachel","racial","racing","rack","racks","radar",
"radiation","radical","radio","radios","radius","rage","raid","rail",
"railroad","railway","rain","rainbow","raise","raised","raises","raising",
"raleigh","rally","ralph","ranch","rand","random","randy","range",
"rangers","ranges","ranging","rank","ranked","ranking","rankings","ranks",
"rape","rapid","rapidly","rapids","rare","rarely","rate","rated",
"rates","rather","rating","ratings","ratio","rational","ratios","rats",
"raymond","rays","reach","reached","reaches","reaching","reaction","reactions",
"read","reader","readers","readily","reading","readings","reads","ready",
"real","realistic","reality","realize","realized","really","realm","realtor",
"realtors","realty","rear","reason","reasonable","reasonably","reasoning","reasons",
"rebate","rebates","rebecca","rebel","rebound","recall","receipt","receive",
"received","receiver","receivers","receives","receiving","recent","recently","reception",
"receptor","receptors","recipe","recipes","recipient","recipients","recognised","recognition",
"recognize","recognized","recommend","recommendation","recommendations","recommended","recommends","reconstruction",
"record","recorded","recorder","recorders","recording","recordings","records","recover",
"recovered","recovery","recreation","recreational","recruiting","recruitment","recycling","redeem",
"redhead","reduce","reduced","reduces","reducing","reduction","reductions","reed",
"reef","reel","refer","reference","referenced","references","referral","referrals",
"referred","referring","refers","refinance","refine","refined","reflect","reflected",
"reflection","reflections","reflects","reform","reforms","refresh","refrigerator","refugees",
"refund","refurbished","refuse","refused","regard","regarded","regarding","regardless",
"regards","reggae","regime","region","regional","regions","register","registered",
"registrar","registration","registry","regression","regular","regularly","regulated","regulation",
"regulations","regulatory","rehab","rehabilitation","reid","reject","rejected","relate",
"related","relates","relating","relation","relations","relationship","relationships","relative",
"relatively","relatives","relax","relaxation","relay","release","released","releases",
"relevance","relevant","reliability","reliable","reliance","relief","religion","religions",
"religious","reload","relocation","rely","relying","remain","remainder","remained",
"remaining","remains","remark","remarkable","remarks","remedies","remedy","remember",
"remembered","remind","reminder","remix","remote","removable","removal","remove",
"removed","removing","renaissance","render","rendered","rendering","renew","renewable",
"renewal","reno","rent","rental","rentals","rentcom","repair","repairs",
"repeat","repeated","replace","replaced","replacement","replacing","replica","replication",
"replied","replies","reply","report","reported","reporter","reporters","reporting",
"reports","repository","represent","representation","representations","representative","representatives","represented",
"representing","represents","reprint","reprints","reproduce","reproduced","reproduction","reproductive",
"republic","republican","republicans","reputation","request","requested","requesting","requests",
"require","required","requirement","requirements","requires","requiring","rescue","research",
"researcher","researchers","reseller","reservation","reservations","reserve","reserved","reserves",
"reservoir","reset","residence","resident","residential","residents","resist","resistance",
"resistant","resolution","resolutions","resolve","resolved","resort","resorts","resource",
"resources","respect","respected","respective","respectively","respiratory","respond","responded",
"respondent","respondents","responding","response","responses","responsibilities","responsibility","responsible",
"rest","restaurant","restaurants","restoration","restore","restored","restrict","restricted",
"restriction","restrictions","restructuring","result","resulted","resulting","results","resume",
"resumes","retail","retailer","retailers","retain","retained","retention","retired",
"retirement","retreat","retrieval","retrieve","retrieved","retro","return","returned",
"returning","returns","reunion","reuters","reveal","revealed","reveals","revelation",
"revenge","revenue","revenues","reverse","review","reviewed","reviewer","reviewing",
"reviews","revised","revision","revisions","revolution","revolutionary","reward","rewards",
"reynolds","rhode","rhythm","ribbon","rica","rice","rich","richard",
"richards","richardson","richmond","rick","rico","ride","rider","riders",
"rides","ridge","riding","right","rights","ring","rings","ringtone",
"ringtones","ripe","rise","rising","risk","risks","river","rivers",
"riverside","road","roads","robert","roberts","robertson","robin","robinson",
"robot","robots","robust","rochester","rock","rocket","rocks","rocky",
"roger","rogers","roland","role","roles","roll","rolled","roller",
"rolling","rolls","roman","romance","romania","romantic","rome","ronald",
"roof","room","roommate","roommates","rooms","root","roots","rope",
"rosa","rose","roses","ross","roster","rotary","rotation","rouge",
"rough","roughly","roulette","round","rounds","route","router","routers",
"routes","routine","routines","routing","rover","rows","royal","royalty",
"rubber","ruby","rugby","rugs","rule","ruled","rules","ruling",
"runner","running","runs","runtime","rural","rush","russell","russia",
"russian","ruth","rwanda","ryan","sacramento","sacred","sacrifice","saddam",
"safari","safe","safely","safer","safety","sage","sagem","said",
"sail","sailing","saint","saints","sake","salad","salaries","salary",
"sale","salem","sales","sally","salmon","salon","salt","salvador",
"salvation","samba","same","samoa","sample","samples","sampling","samsung",
"samuel","sand","sandra","sandwich","sandy","sans","santa","sanyo",
"sapphire","sara","sarah","saskatchewan","satellite","satin","satisfaction","satisfactory",
"satisfied","satisfy","saturday","saturn","sauce","saudi","savage","savannah",
"save","saved","saver","saves","saving","savings","saying","says",
"sbjct","scale","scales","scan","scanned","scanner","scanners","scanning",
"scary","scenario","scenarios","scene","scenes","scenic","schedule","scheduled",
"schedules","scheduling","schema","scheme","schemes","scholar","scholars","scholarship",
"scholarships","school","schools","science","sciences","scientific","scientist","scientists",
"scoop","scope","score","scored","scores","scoring","scotia","scotland",
"scott","scottish","scout","scratch","screen","screening","screens","screensaver",
"screensavers","screenshot","screenshots","screw","script","scripting","scripts","scroll",
"scsi","scuba","sculpture","seafood","seal","sealed","sean","search",
"searchcom","searched","searches","searching","seas","season","seasonal","seasons",
"seat","seating","seats","seattle","second","secondary","seconds","secret",
"secretariat","secretary","secrets","section","sections","sector","sectors","secure",
"secured","securely","securities","security","seed","seeds","seeing","seek",
"seeker","seekers","seeking","seeks","seem","seemed","seems","seen",
"sees","sega","segment","segments","select","selected","selecting","selection",
"selections","selective","self","sell","seller","sellers","selling","sells",
"semester","semi","semiconductor","seminar","seminars","senate","senator","senators",
"send","sender","sending","sends","senegal","senior","seniors","sense",
"sensitive","sensitivity","sensor","sensors","sent","sentence","sentences","separate",
"separated","separately","separation","sept","september","sequence","sequences","serbia",
"serial","series","serious","seriously","serum","serve","served","server",
"servers","serves","service","services","serving","session","sessions","sets",
"setting","settings","settle","settled","settlement","setup","seven","seventh",
"several","severe","sewing","shade","shades","shadow","shadows","shaft","shake","shakespeare",
"shakira","shall","shame","shanghai","shannon","shape","shaped","shapes",
"share","shared","shareholders","shares","shareware","sharing","shark","sharon",
"sharp","shaved","shaw","shed","sheep","sheer","sheet","sheets",
"sheffield","shelf","shell","shelter","shemale","shemales","shepherd","sheriff",
"sherman","shield","shift","shine","ship","shipment","shipments","shipped",
"shipping","ships","shirt","shirts","shock","shoe","shoes",
"shoot","shooting","shop","shopper","shoppercom","shoppers","shopping","shoppingcom",
"shops","shopzilla","shore","short","shortcuts","shorter","shortly","shorts",
"shot","shots","should","shoulder","show","showcase","showed","shower",
"showers","showing","shown","shows","showtimes","shut","shuttle","sick",
"side","sides","siemens","sierra","sight","sigma","sign","signal",
"signals","signature","signatures","signed","significance","significant","significantly","signing",
"signs","signup","silence","silent","silicon","silk","silly","silver",
"similar","similarly","simon","simple","simplified","simply","simpson","simpsons",
"sims","simulation","simulations","simultaneously","since","sing","singapore","singer",
"singh","singing","single","singles","sink","sister","sisters","site",
"sitemap","sites","sitting","situated","situation","situations","sixth","size",
"sized","sizes","skating","skiing","skill","skilled","skills","skin",
"skins","skip","skirt","skirts","skype","slave","sleep","sleeping",
"sleeps","sleeve","slide","slides","slideshow","slight","slightly","slim",
"slip","slope","slot","slots","slovak","slovakia","slovenia","slow",
"slowly","small","smaller","smart","smell","smile",
"smilies","smith","smithsonian","smoke","smoking","smooth","smtp","snake",
"snap","snapshot","snow","snowboard","soap","soccer","social","societies",
"society","sociology","socket","socks","sodium","sofa","soft","softball",
"software","soil","solar","solaris","sold","soldier","soldiers","sole",
"solely","solid","solo","solomon","solution","solutions","solve","solved",
"solving","soma","somalia","some","somebody","somehow","someone","somerset",
"something","sometimes","somewhat","somewhere","song","songs","sonic","sons",
"sony","soon","soonest","sophisticated","sorry","sort","sorted","sorts",
"sought","soul","souls","sound","sounds","soundtrack","soup","source",
"sources","south","southampton","southeast","southern","southwest","soviet","space",
"spaces","spain","spam","span","spanish","spank","spanking","sparc",
"spare","spas","spatial","speak","speaker","speakers","speaking","speaks",
"spears","spec","special","specialist","specialists","specialized","specializing","specially",
"specials","specialties","specialty","species","specific","specifically","specification","specifications",
"specifics","specified","specifies","specify","specs","spectacular","spectrum","speech",
"speeches","speed","speeds","spell","spelling","spencer","spend","spending",
"spent","sperm","sphere","spice","spider","spies","spin","spine",
"spirit","spirits","spiritual","spirituality","split","spoke","spoken","spokesman",
"sponsor","sponsored","sponsors","sponsorship","sport","sporting","sports","spot",
"spotlight","spots","spouse","spray","spread","spreading","spring","springer",
"springfield","springs","sprint","spyware","squad","square","squirt","squirting",
"stability","stable","stack","stadium","staff","staffing","stage","stages",
"stainless","stakeholders","stamp","stamps","stan","stand","standard","standards",
"standing","standings","stands","stanford","stanley","star","starring","stars",
"starsmerchant","start","started","starter","starting","starts","startup","stat",
"state","stated","statement","statements","states","statewide","static","stating",
"station","stationery","stations","statistical","statistics","stats","status","statute",
"statutes","statutory","stay","stayed","staying","stays","steady","steal",
"steam","steel","steering","stem","step","stephanie","stephen","steps",
"stereo","sterling","steve","steven","stevens","stewart","stick","sticker",
"stickers","sticks","sticky","still","stock","stockholm","stockings","stocks",
"stolen","stomach","stone","stones","stood","stop","stopped","stopping",
"stops","storage","store","stored","stores","stories","storm","story",
"straight","strain","strand","strange","stranger","strap","strategic","strategies",
"strategy","stream","streaming","streams","street","streets","strength","strengthen",
"strengthening","strengths","stress","stretch","strict","strictly","strike","strikes",
"striking","string","strings","strip","stripes","strips","stroke","strong",
"stronger","strongly","struck","struct","structural","structure","structured","structures",
"struggle","stuart","stuck","stud","student","students","studied","studies",
"studio","studios","study","studying","stuff","stuffed","stunning","stupid",
"style","styles","stylish","stylus","subaru","subcommittee","subdivision","subject",
"subjects","sublime","sublimedirectory","submission","submissions","submit","submitted","submitting",
"subscribe","subscriber","subscribers","subscription","subscriptions","subsection","subsequent","subsequently",
"subsidiaries","subsidiary","substance","substances","substantial","substantially","substitute","subtle",
"suburban","succeed","success","successful","successfully","such","suck","sucking",
"sucks","sudan","sudden","suddenly","suffer","suffered","suffering","sufficient",
"sufficiently","sugar","suggest","suggested","suggesting","suggestion","suggestions","suggests",
"suicide","suit","suitable","suite","suited","suites","suits","sullivan",
"summaries","summary","summer","summit","sunday","sunglasses","sunny","sunrise",
"sunset","sunshine","super","superb","superintendent","superior","supervision","supervisor",
"supervisors","supplement","supplemental","supplements","supplied","supplier","suppliers","supplies",
"supply","support","supported","supporters","supporting","supports","suppose","supposed",
"supreme","sure","surely","surf","surface","surfaces","surfing","surge",
"surgeon","surgeons","surgery","surgical","surname","surplus","surprise","surprised",
"surprising","surrey","surround","surrounded","surrounding","surveillance","survey","surveys",
"survival","survive","survivor","survivors","susan","suse","suspect","suspected",
"suspended","suspension","sussex","sustainability","sustainable","sustained","suzuki","swap",
"sweden","swedish","sweet","swift","swim","swimming","swing","swingers",
"swiss","switch","switched","switches","switching","switzerland","sword","sydney",
"symantec","symbol","symbols","sympathy","symphony","symposium","symptoms","sync",
"syndicate","syndication","syndrome","synopsis","syntax","synthesis","synthetic","syracuse",
"syria","system","systematic","systems","table","tables","tablet","tablets",
"tabs","tackle","tactics","tagged","tags","tahoe","tail","taiwan",
"take","taken","takes","taking","tale","talent","talented","tales",
"talk","talked","talking","talks","tall","tamil","tampa","tank",
"tanks","tanzania","tape","tapes","target","targeted","targets","tariff",
"task","tasks","taste","tattoo","taught","taxation","taxes","taxi",
"taylor","teach","teacher","teachers","teaches","teaching","team","teams",
"tear","tears","tech","technical","technician","technique","techniques","techno",
"technological","technologies","technology","techrepublic","teddy","teen","teenage","teens",
"teeth","telecharger","telecom","telecommunications","telephone","telephony","telescope","television",
"televisions","tell","telling","tells","temp","temperature","temperatures","template",
"templates","temple","temporal","temporarily","temporary","tenant","tend","tender",
"tennessee","tennis","tension","tent","term","terminal","terminals","termination",
"terminology","terms","terrace","terrain","terrible","territories","territory","terror",
"terrorism","terrorist","terrorists","terry","test","testament","tested","testimonials",
"testimony","testing","tests","texas","text","textbook","textbooks","textile",
"textiles","texts","texture","thai","thailand","than","thank","thanks",
"thanksgiving","that","thats","theater","theaters","theatre","thee","theft",
"thehun","their","them","theme","themes","themselves","then","theology",
"theorem","theoretical","theories","theory","therapeutic","therapist","therapy","there",
"thereafter","thereby","therefore","thereof","thermal","thesaurus","these","thesis",
"they","thick","thickness","thin","thing","things","think","thinking",
"thinkpad","thinks","third","thirty","this","thomas","thompson","thomson",
"thong","thongs","thorough","thoroughly","those","thou","though","thought",
"thoughts","thousand","thousands","thread","threaded","threads","threat","threatened",
"threatening","threats","three","threesome","threshold","thriller","throat","through",
"throughout","throw","throwing","thrown","throws","thru","thumb","thumbnail",
"thumbnails","thumbs","thumbzilla","thunder","thursday","thus","ticket","tickets",
"tide","tied","tier","ties","tiffany","tiger","tigers","tight",
"tile","tiles","till","timber","time","timeline","timely","timer",
"times","timing","timothy","tiny","tion","tions","tips","tire",
"tired","tires","tissue","titanium","titans","title","titled","titles",
"titten","tobacco","tobago","today","todd","toddler","together",
"toilet","token","tokyo","told","tolerance","toll","tomato","tomatoes",
"tommy","tomorrow","tone","toner","tones","tongue","tonight","tons",
"tony","took","tool","toolbar","toolbox","toolkit","tools","tooth",
"topic","topics","topless","tops","toronto","torture","toshiba","total",
"totally","totals","touch","touched","tough","tour","touring","tourism",
"tourist","tournament","tournaments","tours","toward","towards","tower","towers",
"town","towns","township","toxic","toyota","toys","trace","track",
"trackback","trackbacks","tracked","tracker","tracking","tracks","tract","tractor",
"tracy","trade","trademark","trademarks","trader","trades","trading","tradition",
"traditional","traditions","traffic","tragedy","trail","trailer","trailers","trails",
"train","trained","trainer","trainers","training","trains","tramadol","trance",
"tranny","trans","transaction","transactions","transcript","transcription","transcripts","transexual",
"transexuales","transfer","transferred","transfers","transform","transformation","transit","transition",
"translate","translated","translation","translations","translator","transmission","transmit","transmitted",
"transparency","transparent","transport","transportation","transsexual","trap","trash","trauma",
"travel","traveler","travelers","traveling","traveller","travelling","travels","travesti",
"travis","tray","treasure","treasurer","treasures","treasury","treat","treated",
"treating","treatment","treatments","treaty","tree","trees","trek","trembl",
"tremendous","trend","trends","treo","trial","trials","triangle","tribal",
"tribe","tribes","tribunal","tribune","tribute","trick","tricks","tried",
"tries","trigger","trim","trinidad","trinity","trio","trip","tripadvisor",
"triple","trips","triumph","trivia","troops","tropical","trouble","troubleshooting",
"trout","troy","truck","trucks","true","truly","trunk","trust",
"trusted","trustee","trustees","trusts","truth","trying","tsunami","tube",
"tubes","tucson","tuesday","tuition","tulsa","tumor","tune","tuner",
"tunes","tuning","tunisia","tunnel","turbo","turkey","turkish","turn",
"turned","turner","turning","turns","turtle","tutorial","tutorials","tvcom",
"twelve","twenty","twice","twiki","twin","twinks","twins","twist",
"twisted","tyler","type","types","typical","typically","typing","uganda",
"ugly","ukraine","ultimate","ultimately","ultra","ultram","unable","unauthorized",
"unavailable","uncertainty","uncle","undefined","under","undergraduate","underground","underlying",
"understand","understanding","understood","undertake","undertaken","underwear","undo","unemployment",
"unexpected","unfortunately","unified","uniform","union","unions","uniprotkb","unique",
"unit","united","units","unity","univ","universal","universe","universities",
"university","unix","unknown","unless","unlike","unlikely","unlimited","unlock",
"unnecessary","unsigned","unsubscribe","until","untitled","unto","unusual","unwrap",
"upcoming","update","updated","updates","updating","upgrade","upgrades","upgrading",
"upload","uploaded","upon","upper","upset","upskirt","upskirts","urban",
"urge","urgent","urls","uruguay","usage","usda","used","useful",
"user","username","users","uses","usgs","using","usps","usual",
"usually","utah","utilities","utility","utilization","utilize","utils","uzbekistan",
"vacancies","vacation","vacations","vaccine","vacuum","valentine","valid",
"validation","validity","valium","valley","valuable","valuation","value","valued",
"values","valve","valves","vampire","vancouver","vanilla","variable","variables",
"variance","variation","variations","varied","varies","variety","various","vary",
"varying","vast","vatican","vault","vbulletin","vector","vegas","vegetable",
"vegetables","vegetarian","vegetation","vehicle","vehicles","velocity","velvet","vendor",
"vendors","venezuela","venice","venture","ventures","venue","venues","verbal",
"verde","verification","verified","verify","verizon","vermont","vernon","verse",
"version","versions","versus","vertex","vertical","very","verzeichnis","vessel",
"vessels","veteran","veterans","veterinary","viagra","vibrator","vibrators","vice",
"victim","victims","victor","victoria","victorian","victory","video","videos",
"vids","vienna","vietnam","vietnamese","view","viewed","viewer","viewers",
"viewing","viewpicture","views","viii","viking","villa","village","villages",
"villas","vincent","vintage","vinyl","violation","violations","violence","violent",
"violin","viral","virgin","virginia","virtual","virtually","virtue","virus",
"viruses","visa","visibility","visible","vision","visit","visited","visiting",
"visitor","visitors","visits","vista","visual","vital","vitamin","vitamins",
"vocabulary","vocal","vocals","vocational","voice","voices","void","voip",
"volkswagen","volleyball","volt","voltage","volume","volumes","voluntary","volunteer",
"volunteers","volvo","vote","voted","voters","votes","voting","voyeur",
"voyeurweb","voyuer","vsnet","vulnerability","vulnerable","wage","wages","wagner",
"wagon","wait","waiting","waiver","wake","wales","walk","walked",
"walker","walking","walks","wall","wallace","wallet","wallpaper","wallpapers",
"walls","walnut","walt","walter","wang","wanna","want","wanted",
"wanting","wants","warcraft","ward","ware","warehouse","warm","warming",
"warned","warner","warning","warnings","warrant","warranties","warranty","warren",
"warrior","warriors","wars","wash","washer","washing","washington","waste",
"watch","watched","watches","watching","water","waterproof","waters","watershed",
"watson","watt","watts","wave","waves","wayne","ways","weak",
"wealth","weapon","weapons","wear","wearing","weather","webcam","webcams",
"webcast","weblog","weblogs","webmaster","webmasters","webpage","webshots","website",
"websites","webster","wedding","weddings","wednesday","weed","week","weekend",
"weekends","weekly","weeks","weight","weighted","weights","weird","welcome",
"welding","welfare","well","wellington","wellness","wells","welsh","wendy",
"went","were","wesley","west","western","westminster","whale","what",
"whatever","whats","wheat","wheel","wheels","when","whenever","where",
"whereas","wherever","whether","which","while","whilst","white","whole",
"wholesale","whom","whose","wichita","wicked","wide","widely",
"wider","widescreen","widespread","width","wife","wifi","wiki","wikipedia",
"wild","wilderness","wildlife","wiley","will","william","williams","willing",
"willow","wilson","wind","window","windows","winds","windsor","wine",
"wines","wing","wings","winner","winners","winning","wins","winston",
"winter","wire","wired","wireless","wires","wiring","wisconsin","wisdom",
"wise","wish","wishes","wishlist","witch","with","withdrawal","within",
"without","witness","witnesses","wives","wizard","wolf","woman","women",
"womens","wonder","wonderful","wondering","wood","wooden","woods","wool",
"worcester","word","wordpress","words","work","worked","worker","workers",
"workflow","workforce","working","workout","workplace","works","workshop","workshops",
"workstation","world","worldcat","worlds","worldsex","worldwide","worm","worn",
"worried","worry","worse","worship","worst","worth","worthy","would",
"wound","wrap","wrapped","wrapping","wrestling","wright","wrist","write",
"writer","writers","writes","writing","writings","written","wrong","wrote",
"wyoming","xanax","xbox","xerox","xhtml","xnxx","yacht","yahoo",
"yale","yamaha","yang","yard","yards","yarn","yeah","year",
"yearly","years","yeast","yellow","yemen","yesterday","yield","yields",
"yoga","york","yorkshire","young","younger","your","yours","yourself",
"youth","yugoslavia","yukon","zambia","zdnet","zealand","zero","zimbabwe",
"zinc","zoloft","zone","zones","zoning","zoom","zoophilia","zope",
"zshops")

def defaultVars():
    global beenPlantation
    global beenUpclose
    global beenField
    global beenVillage1
    global beenVillage2
    global beenVillage3
    global beenBunker
    global beenLibrary
    global beenBaldbasementEntrance
    global beenHouseEntrance
    global beenLivingRoom
    global beenUpstairs
    global beenSafeRoom
    global beenSafe
    global beenBackyard
    global beenBasement
    global beenCellar
    global beenSwamp
    global beenDojoExt
    global beenDojoInt
    global beenIntersection
    global beenJunkyard
    global beenJunkyardDeep
    global beenMonkeyMan
    global beenBlue
    global beenRed
    global beenGreen

    global textPlay
    global firstTimePlantation
    global hasKnowledge
    global hasKO
    global hasBlue
    global hasRed
    global hasGreen
    global hasKnocked
    global safeCracked
    global hasShovel
    global hasOranges
    global password
    global blueOpen
    global redOpen
    global greenOpen

    global northBind
    global eastBind
    global southBind
    global westBind

    beenPlantation = False
    beenUpclose = False
    beenField = False
    beenVillage1 = False
    beenVillage2 = False
    beenVillage3 = False
    beenBunker = False
    beenLibrary = False
    beenBaldbasementEntrance = False
    beenHouseEntrance = False
    beenLivingRoom = False
    beenUpstairs = False
    beenSafeRoom = False
    beenSafe = False
    beenBackyard = False
    beenBasement = False
    beenCellar = False
    beenSwamp = False
    beenDojoExt = False
    beenDojoInt = False
    beenIntersection = False
    beenJunkyard = False
    beenJunkyardDeep = False
    beenMonkeyMan = False
    beenBlue = False
    beenRed = False
    beenGreen = False

    textPlay = True
    firstTimePlantation = True
    hasKnowledge = False
    hasKO = False
    hasBlue = False
    hasRed = False
    hasGreen = False
    hasKnocked = False
    safeCracked = False
    hasShovel = False
    hasOranges = False
    blueOpen = False
    redOpen = False
    greenOpen = False
    password = random.choice(wordlist)

    northBind = root.bind("<w>", lambda z: unbinded())
    eastBind = root.bind("<d>", lambda z: unbinded())
    southBind = root.bind("<s>", lambda z: unbinded())
    westBind = root.bind("<a>", lambda z: unbinded())


defaultVars()



mainloop()
