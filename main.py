import math
import numbers

class Army:

    def __init__(self, soldiers = 0, equip = 0, training = 0, mor = 0):
        self.numSoldiers = soldiers
        self.equipScore = equip
        self.trainingScore = training
        self.morale = mor
        self.combatEffectiveness = 0

    def setCombatEffectiveness(self):
        self.combatEffectiveness = math.log((((self.numSoldiers * self.equipScore) + self.trainingScore)*self.morale),100) * 10


class Player:
    def __init__(self, city, gold):
        self.currentCity = city
        self.playerGold = gold
        self.army = Army()

    def setCity(self, city):
        self.currentCity = city

def buildMenu(cities, currentCity):
    menuList = []
    menuPos = 0
    # Add city travel options
    for i in range(4):
        if i != currentCity:
            menuList.insert(menuPos, [(str(menuPos) + ". Travel to " + cities[i]),i])
            menuPos += 1
    # Add raise army option
    menuList.insert(menuPos, [str(menuPos) + ". Raise army in " + cities[currentCity]])
    menuPos += 1
    return menuList

def printMenu(menuList):
    largestMenuItem = 0
    # Get the length of the largest menu item
    for item in menuList:
        if len(item[0]) > largestMenuItem:
            largestMenuItem = len(item[0])
    # Print menu header
    for i in range(largestMenuItem):
        print("=", end = "")
    # Print a newline
    print()
    # Print the actual menu
    for item in menuList:
        print(item[0])
    # Print the menu footer
    for i in range(largestMenuItem):
        print("-", end = "")
    # Print a newline
    print()

def getDistance(city1, city2):
    for list in cityGraph:
        if list[0] == city1 and list[1] == city2:
            return list[2]
    return 0

def getPlayerChoice(msg):
    try:
        inp = int(input(msg))
    except:
        inp = -1
    return inp

#def combatEffectiveness(numbers, equipment, training, morale):
#    return math.log((((numbers * equipment) + training)*morale),100) * 10

# Create the list of cities and the graph of distances between them
cities = ["Luxemburg","Leaf","Washington","Rat's Nest"]
cityGraph = [[cities[0],cities[1],4],
             [cities[0],cities[2],3],
             [cities[0],cities[3],3],
             [cities[1],cities[0],4],
             [cities[1],cities[2],3],
             [cities[1],cities[3],6],
             [cities[2],cities[0],3],
             [cities[2],cities[1],3],
             [cities[2],cities[3],3],
             [cities[3],cities[0],3],
             [cities[3],cities[1],6],
             [cities[3],cities[2],3]]

#dist = getDistance(cities[0],cities[3])
#print("Distance", dist)

#usArmy = Army(1400000,2,500,10) # US Army
#usArmy.setCombatEffectiveness()
#print("US Army Combat Effectivness: ", usArmy.combatEffectiveness)

#sarumanArmy = Army(10000,1.5,100,2)
#sarumanArmy.setCombatEffectiveness()
#print("Saruman Army Combat Effectiveness: ", sarumanArmy.combatEffectiveness)

#playerOne = Player(1, 100)
#print("Player One Army Combat Effectiveness: ", playerOne.army.combatEffectiveness)

#print("Combat Effectiveness", combatEffectiveness(300,1.2,100,1))
playerOne = Player(1, 100)
# Main Game Loop
while(True):
    # build menu
    menu = buildMenu(cities, playerOne.currentCity)
    # print menu
    printMenu(menu)
    # get player choice
    while(True):
        choice = getPlayerChoice("Make a selection: ")
        #print("You chose", choice)
        # Make travel function
        if choice != -1:
            if choice == 0:
                print("Traveling to", cities[menu[0][1]])
                playerOne.setCity(menu[0][1])
                break
            elif choice == 1:
                print("Traveling to", cities[menu[1][1]])
                playerOne.setCity(menu[1][1])
                break
            elif choice == 2:
                print("Traveling to", cities[menu[2][1]])
                playerOne.setCity(menu[2][1])
                break
            elif choice == 3:
                exit()
        print("Invalid selection")
        # do player choice
        # increment computer player stat(s)

