import random
random.seed()   #Prepare random number generator

box1 = " "
box2 = " "
box3 = " "
moveCount = 0
gameOver = False
chosenBox = 0
startChoice = int(random.random() * 2) + 1
if startChoice == 1:
    currentPlayer = "O"
    print("Coin Toss: User (O) goes first!")
else:
    currentPlayer = "X"
    print("Coin Toss: Computer (X) goes first!")
while gameOver == False and moveCount < 3:
    print("[" + box1 + " | " + box2 + " | " + box3 + "]")
    if currentPlayer == "O":
        validMove = False
        while validMove == False:
            print("Enter box number (1, 2, or 3):")
            chosenBox = int(input())
            if chosenBox == 1 and box1 == " ":
                box1 = "X"
                validMove = True
            else:
                if chosenBox == 2 and box2 == " ":
                    box2 = "X"
                    validMove = True
                else:
                    if chosenBox == 3 and box3 == " ":
                        box3 = "X"
                        validMove = True
                    else:
                        print("Invalid choice or box taken! Try again.")
    else:
        validMove = False
        while validMove == False:
            chosenBox = int(random.random() * 3) + 1
            if chosenBox == 1 and box1 == " ":
                box1 = "X"
                validMove = True
            else:
                if chosenBox == 2 and box2 == " ":
                    box2 = "X"
                    validMove = True
                else:
                    if chosenBox == 3 and box3 == " ":
                        box3 = "X"
                        validMove = True
        print("Computer played box " + str(chosenBox))
    moveCount = moveCount + 1
    if box1 == box2 and box2 == box3 and box1 != " ":
        print("FINAL BOARD: [" + box1 + " | " + box2 + " | " + box3 + "]")
        print("GAME OVER! Computer wins!")
        gameOver = True
    else:
        if moveCount == 3:
            print("FINAL BOARD: [" + box1 + " | " + box2 + " | " + box3 + "]")
            print("GAME OVER! It is a draw!")
            gameOver = True
        else:
            if currentPlayer == "O":
                currentPlayer = "X"
            else:
                currentPlayer = "O"
