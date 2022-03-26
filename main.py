# -----------------------------------------------------------------------------
# Name:        Karate Simulator (main.py)
# Purpose:     Provide a 1v1 karate simulation
#
# Author:      Omer Khan
# Created:     9-March-2022
# Updated:     25-March-2022
# -----------------------------------------------------------------------------

print("This simulation is best experienced with the console tab fully open.")

from tabulate import tabulate
#Ask user if they want to see tutorial
seeTutorial = input("Would you like to see the tutorial? ")
while seeTutorial != "yes" and seeTutorial != "no":
    print("Please choose between a 'yes' or 'no' ")
    seeTutorial = input("Would you like to see the tutorial? ").strip().lower()
if seeTutorial == "yes":
    print(
        "Tutorial: Welcome to Karate Simulator. This tutorial will teach you how to use the simulation. Below this text is a table. Each column starts with the name of a move. Going further down the column will display specific information about the move depending on the row. There are 3 types of moves: Attack, Block, and Rest. They all have their unique functions. Attack effects the opponents health negatively and affects your energy negatively. Block reduces the opponents attack by a certain percentage(that is if they choose an Attack move) and effects your energy negatively(not as much as Attack though). Rest effects your health and energy positively. Furthermore, you also have the option to edit this default preset to your preferences. And thats all there is to it. Your now ready to venture into the world of karate. Good Luck!"
    )

#Setup and output moves table
defuaultMoves = {
    "Straight Punch": [-15, "-13", "Attack"],
    "Front Kick": [-20, "-30", "Attack"],
    "Downward Block": ["60% of opponent's attack", "-6", "Block"],
    "Middle Block": ["80% of opponent's attack", "-10", "Block"],
    "Rest": [25, "+20", "Rest"],
}

rowList = ["Health Effect", "Energy Effect", "Move Type"]

print(
    tabulate(defuaultMoves,
             headers='keys',
             tablefmt='fancy_grid',
             showindex=rowList))

userWantToEdit = input(
    "Would you like to edit the defualt moves: ").strip().lower()

#Ask user if they want to edit defualt moves list
while userWantToEdit != "yes" and userWantToEdit != "no":
    print("Please choose between a 'yes' or 'no' ")
    userWantToEdit = input(
        "Would you like to edit the defualt moves: ").strip().lower()

while userWantToEdit == "yes":
    #Ask if they want to modify, remove, or add to the list.
    typeOfEdit = input(
        "'Modify' or 'Remove' an already exisiting move, or 'Add' a new move: "
    ).strip().lower()
    while typeOfEdit != "add" and typeOfEdit != "remove" and typeOfEdit != "modify":
        print("Please choose between 'add', 'remove', or 'edit'.")
        typeOfEdit = input(
            "'Modify' or 'Remove' an already exisiting move, or 'Add' a new move: "
        ).strip().lower()
    if typeOfEdit == "add":
        #Ask for user for which move type they want to add
        moveType = input(
            "Please choose which move type you would like to add: ").strip(
            ).lower()
        while moveType != "attack" and moveType != "block" and moveType != "rest":
            print("Please choose between 'attack', 'block', and 'rest'.")
            moveType = input(
                "Please choose which move type you would like to add: ").strip(
                ).lower()
        if moveType == "attack":
            #Ask user for move types info while enforcing input restrictions
            moveName = input("Please state the name of your new move: ")
            energy = int(input("Please state the energy usage of this move: "))
            while energy > 100 or energy < 0:
                print("Please choose a number between 0 and 100")
                energy = int(input("Please energy usage of this move: "))
            damage = int(input("Please state the damage done by this move: "))
            while damage > 100 or damage < 0:
                print("Please choose a number between 0 and 100")
                damage = int(
                    input("Please state the damage done by this move: "))
            #Add move to the list appropriately
            defuaultMoves[moveName] = [damage * -1, str(energy * -1), "Attack"]

        if moveType == "rest":
            #Ask user for move types info while enforcing input restrictions
            moveName = input("Please state the name of your new move: ")
            energy = int(input("Please state the energy gain of this move: "))
            while energy > 100 or energy < 0:
                print("Please choose a number between 0 and 100")
                energy = int(input("Please energy usage of this move: "))
            healthGain = int(
                input("Please state the health gained from this move: "))
            while healthGain > 100 or healthGain < 0:
                print("Please choose a number between 0 and 100")
                healthGain = int(
                    input("Please state the damage done by this move: "))
            #Add move to the list appropriately
            defuaultMoves[moveName] = [healthGain, "+" + str(energy), "Rest"]
        if moveType == "block":
            #Ask user for move types info while enforcing input restrictions
            moveName = input("Please state the name of your new move: ")
            energy = int(input("Please energy usage of this move: "))
            while energy > 100 or energy < 0:
                print("Please choose a number between 0 and 100")
                energy = int(
                    input("Please state the energy usage of this move: "))
            blockPercent = int((input(
                "Please state the block percent of this move: ").strip("%")))
            while blockPercent > 100 or blockPercent < 0:
                print("Please choose a number between 0 and 100")
                blockPercent = int(
                    input("Please state the block percent of this move: ").
                    strip("%"))
            #Add move to the list appropriately
            defuaultMoves[moveName] = [
                str(blockPercent) + "% of opponent's attack ",
                str(energy * -1), "Block"
            ]
    elif typeOfEdit == "remove":
        #Ask user which move they want to remove and confirm that the move inputted exists.
        choosenMove = input("What move do you want to remove: ")
        while choosenMove not in defuaultMoves.keys():
            print("Please make sure your choosen move already exists.")
            choosenMove = input("What move do you want to remove: ")
        #Remove move from list
        del defuaultMoves[choosenMove]
        print(choosenMove + " has been successfully removed!")
    elif typeOfEdit == "modify":
        #Ask user which move they want to modify and confirm that the move inputted exists
        choosenMove = input("What move do you want to modify: ")
        while choosenMove not in defuaultMoves.keys():
            print("Please make sure your choosen move already exists.")
            choosenMove = input("What move do you want to modify: ")
        modifyInfo = input("Which information do you want to change? ")
        while modifyInfo != "Health Effect" and modifyInfo != "Energy Effect":
            print("Please choose between 'Health Effect' or 'Energy Effect'")
            modifyInfo = input("Which information do you want to change? ")
        if modifyInfo == "Health Effect":

            if defuaultMoves[choosenMove][2] == "Attack":
                #Ask user for moves health effect while enforcing input restrictions
                healthEffect = int(
                    input("Please state the health effect of this move: "))
                while healthEffect > 100 or healthEffect < 0:
                    print("Please choose a number between 0 and 100")
                    healthEffect = int(
                        input("Please state the health effect of this move: "))
                #Change the damage of the choosen move
                defuaultMoves[choosenMove][0] = healthEffect * -1
            elif defuaultMoves[choosenMove][2] == "Block":
                #Ask user for moves block percent while enforcing input restrictions
                blockPercent = int(
                    (input("Please state the block percent of this move: ").
                     strip("%")))
                while blockPercent > 100 or blockPercent < 0:
                    print("Please choose a number between 0 and 100")
                    blockPercent = int(
                        input("Please state the block percent of this move: ").
                        strip("%"))
                #Change the block percent of the choosen move
                defuaultMoves[choosenMove][0] = str(
                    blockPercent) + "% of opponent's attack "
            elif defuaultMoves[choosenMove][2] == "Rest":
                #Ask user for moves health gain while enforcing input restrictions
                healthEffect = int(
                    input("Please state the health effect of this move: "))
                while healthEffect > 100 or healthEffect < 0:
                    print("Please choose a number between 0 and 100")
                    healthEffect = int(
                        input("Please state the health effect of this move: "))
                #Change the health gain of the choosen move
                defuaultMoves[choosenMove][0] = healthEffect
        elif modifyInfo == "Energy Effect":
            if defuaultMoves[choosenMove][2] == "Attack" or defuaultMoves[
                    choosenMove][2] == "Block":
                #Ask user for moves energy usage while enforcing input restrictions
                energyUsage = int(
                    input("Please state energy usage of this move: "))
                while energyUsage > 100 or energyUsage < 0:
                    print("Please choose a number between 0 and 100")
                    energyUsage = int(
                        input("Please state the energy usage of this move: "))
                #Change the health usage of the choosen move
                defuaultMoves[choosenMove][1] = str(energyUsage * -1)

            elif defuaultMoves[choosenMove][2] == "Rest":
                #Ask user for moves energy gain while enforcing input restrictions
                energyGain = int(
                    input("Please state the energy gain of this move: "))
                while energyGain > 100 or energyGain < 0:
                    print("Please choose a number between 0 and 100")
                    energyGain = int(
                        input("Please state the energy gain of this move: "))
                #Change the health gain of the choosen move
                defuaultMoves[choosenMove][1] = "+" + str(energyGain)
    #Ask user if they want to continue editing while enforcing input restrictions
    continueEditing = input(
        "Would you like to continue editing the moves list? ")
    while continueEditing != "yes" and continueEditing != "no":
        print("Please choose between a 'yes' or 'no' ")
        userWantToEdit = input(
            "Would you like to edit the defualt moves: ").strip().lower()
    if continueEditing == "no":
        #Break user out of list edit loop
        userWantToEdit = "no"

#[Health, Energy]
userStats = [100, 100]
opponentStats = [100, 100]

while userStats[0] > 0 and opponentStats[0] > 0:
    print("\n")
    print(
        tabulate(defuaultMoves,
                 headers='keys',
                 tablefmt='fancy_grid',
                 showindex=rowList))
    #---These varibles reset every loop. They allow the 'block' move to work.---
    #[Health, Energy]
    temporaryUserHealthEffect = 0
    temporaryOpponentHealthEffect = 0
    #[User, Opponent]
    blockFactors = [1, 1]
    #[User, Opponent]
    AttackEffects = [0, 0]
    #-------------------
    userPerspective = "User"
    opponentPerspective = "Opponenet"
    desiredAction = input("What is your desired action? ")
    #Check if move exists
    while desiredAction not in defuaultMoves.keys():
        print("Please choose a valid action")
        desiredAction = input("What is your desired action? ")
        print("\n")
    #If the move choosen is not a 'Rest' type, check if user has enough energy to use the move
    while int(str(defuaultMoves[desiredAction][1]).strip(
            "-")) >= userStats[1] and int(defuaultMoves[desiredAction][1]) < 0:
        print("You don't enough energy!")
        desiredAction = input("What is your desired action? ")
        print("\n")
    aiGoneYet = False

    while aiGoneYet == False:
        if userPerspective == "User":
            healthEffect = defuaultMoves.get(desiredAction)[0]
            #Check if desired action is attack, block, or rest
            if type(healthEffect) == str:
                #Move is block
                blockFactor = int(
                    healthEffect.strip("% of opponent's attack")) / 100
                #Add block percent to block factors list
                blockFactors[0] = blockFactor
                #Decrease users energy
                userStats[1] += int(defuaultMoves.get(desiredAction)[1])

            elif type(healthEffect) == int:
                if healthEffect < 0:
                    #Move is attack
                    #Add damage done to Attack Effects list
                    AttackEffects[0] += healthEffect
                    #Decrease users energy
                    userStats[1] += int(defuaultMoves.get(desiredAction)[1])

                elif healthEffect >= 0:
                    #Move is rest
                    temporaryUserHealthEffect += healthEffect
                    #Increase users energy
                    userStats[1] += int(defuaultMoves.get(desiredAction)[1])
            #Apply energy cap of 100
            if userStats[1] > 100:
                userStats[1] = 100

            #Change perspective
            userPerspective = "Opponenet"
            opponentPerspective = "User"

        if userPerspective == "Opponenet":
            #Follow variable will be set to the move the AI chooses. It follows the format of what .items() returns.
            bestChoice = ("Move Name", [0, 0, 0])
            #Choose best rest if opponent has less then a certain amount of health or energy
            if opponentStats[0] < 20 or opponentStats[1] < 25:
                for actions in defuaultMoves.items():
                    if type(actions[1][0]) == int:
                        if actions[1][0] >= 0:
                            #Update best choice if current best choice is less effective than 'actions' health effect
                            if bestChoice[1][0] < actions[1][0]:
                                bestChoice = actions
                temporaryOpponentHealthEffect += bestChoice[1][0]
                #Reduce opponent energy based off bestChoice
                opponentStats[1] += int(bestChoice[1][1])
                #Apply energy cap of 100
                if opponentStats[1] > 100:
                    opponentStats[1] = 100

            else:
                #Choose best attack if AI's health is greater than or equal to users health
                if opponentStats[0] >= userStats[0]:
                    for actions in defuaultMoves.items():

                        if type(actions[1][0]) == int:
                            #Check if 'actions' health effect value belongs to a attack move.
                            if actions[1][0] < 0:
                                #check if AI has enough energy
                                if int(actions[1][1]) * -1 <= opponentStats[1]:

                                    #Update best choice if current best choice is less effective than 'actions' health effect
                                    if bestChoice[1][0] > actions[1][0]:
                                        bestChoice = actions

                    AttackEffects[1] += bestChoice[1][0]
                    #Reduce opponent energy based off bestChoice
                    opponentStats[1] += int(bestChoice[1][1])
                    #choose deadliest attack
                else:
                    for actions in defuaultMoves.items():
                        #Choose best block
                        if type(actions[1][0]) == str:

                            blockFactor = int(actions[1][0].strip(
                                "% of opponent's attack")) / 100
                            #Check if AI has enough energy to use the block
                            if int(actions[1][1]) <= opponentStats[1]:
                                #Update best choice if current best choice is less effective than 'actions' block percent
                                if blockFactors[1] < blockFactor:
                                    bestChoice = actions

                                    blockFactors[1] = blockFactor
                                #Prevent issues when blockFactors = 1 and a block move is selected
                                if blockFactors[1] == 1:
                                    blockFactors[1] = blockFactor
                    #Reduce opponent energy based off bestChoice
                        opponentStats[1] -= int(bestChoice[1][1])
                    #Apply energy cap of 100
                    if opponentStats[1] > 100:
                        opponentStats[1] = 100

            aiGoneYet = True
            bestChoice = bestChoice[0]
    #Calculate total damage done by taking raw damage done and block percent into consideration
    temporaryUserHealthEffect += AttackEffects[1] * blockFactors[0]
    temporaryOpponentHealthEffect += AttackEffects[0] * blockFactors[1]
    #Add health calculations to user and opponent's health.
    userStats[0] += temporaryUserHealthEffect
    opponentStats[0] += temporaryOpponentHealthEffect

    #Precautions, to avoid any bugs
    if userStats[0] > 100:
        userStats[0] = 100

    if opponentStats[0] > 100:
        opponentStats[0] = 100
    #Output choosen moves
    print("You choose: " + desiredAction)
    print("Your opponent choose: " + bestChoice)
    if userStats[0] > 0 and opponentStats[0] > 0:
        #Output user health, energy, and opponent energy.
        print("You now have " + str(userStats[0]) + " health and " +
              str(userStats[1]) + " energy")
        print("Your opponent now has " + str(opponentStats[0]) + " health")
#End fight if someone has less than or equal to 0 health
if userStats[0] > 0 and opponentStats[0] <= 0:
    print("You have won!")
elif userStats[0] <= 0 and opponentStats[0] > 0:
    print("Your opponent has won!")
elif userStats[0] == opponentStats[0]:
    print("Draw!")
