import random

userInput = input("Let's play my dice rolling simulator! [Y/N] ")

if userInput.lower() == "n":
    print("Ok, see you next time!")

else:
    print("How many virtual dice you want to roll(1-5)")

    try:
            diceCount = int(input("You chose: "))

            if diceCount == 1:
                rollDice = random.randint(1,6)
                print("You rolled: ", rollDice)
            elif diceCount == 2:
                rollDice = random.randint(1,12)
                print("You rolled: ", rollDice)
            elif diceCount == 3:
                rollDice = random.randint(1,18)
                print("You rolled: ", rollDice)
            elif diceCount == 4:
                rollDice = random.randint(1,24)
                print("You rolled: ", rollDice)
            elif diceCount == 5:
                rollDice = random.randint(1,30)
                print("You rolled: ", rollDice)
            else:
                print("Number of dice should be between 1 and 5, Please try again!")

    except ValueError:
            print ("Please Insert a valid value (only numbers allowed)")