"""This is a tic-tac-toe game, played between two players. Game will stop after one of the player win."""

# main matrix pattern on which we will generate our matrix.
matrix = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

# two values for two player
symbl1 = 'O'
symbl2 = 'X'


# win possibility variables
winPossibility = {
    1: {1: None, 2: None, 3: None}, 2: {4: None, 5: None, 6: None}, 3: {7: None, 8: None, 9: None},
    4: {1: None, 4: None, 7: None}, 5: {2: None, 5: None, 8: None}, 6: {3: None, 6: None, 9: None},
    7: {1: None, 5: None, 9: None}, 8: {3: None, 5: None, 7: None}
}


def matrixPattern(matrix):
    """displays the structure of the tic-tac-toe matrix"""
    print("\n")
    print("Matrix".center(10, '*'))
    print("{} | {} | {}".format(matrix[1], matrix[2], matrix[3]))
    print("- - - - -")
    print("{} | {} | {}".format(matrix[4], matrix[5], matrix[6]))
    print("- - - - -")
    print("{} | {} | {}".format(matrix[7], matrix[8], matrix[9]))


def userNameInput(symbl1, symbl2):
    """input player name from user"""
    player1 = input("\nFor [{}] Enter player{} name : ".format(symbl1, 1))
    player2 = input("\nFor [{}] Enter player{} name : ".format(symbl2, 2))
    return player1, player2


def playerMove(player, symbl):
    """calculates the movement of player"""
    playerLoc = input("\n[{}] - Enter location of '{}' : ".format(player, symbl))

    corr_loc = locationCheck(playerLoc, player, symbl)

    if corr_loc == True:
        win = checkWinPos(symbl, playerLoc, player)
        return win


def locationCheck(location, player, symbl):
    """function to check the location which user is inputting"""
    key = list(set(matrix.keys()))
    val = list(set(matrix.values()))

    """This if-condition checks if user is inputting correct value which is between 1 & 9"""

    if key.count(int(location)) == 0:
        print("Wrong location entered, location should be between 1 & 9.")
        playerMove(player, symbl)
    else:

        """This if-condition checks if the current location is occupied or not"""

        if matrix[int(location)] != ' ':
            print("This location is already occupied. Enter Another location of '{}'.".format(symbl))
            playerMove(player, symbl)
        else:
            matrix[int(location)] = symbl
            matrixPattern(matrix)
            return True


def checkWinPos(symbl, position, player):
    """checks if the player is winning, if yes then game terminates with correct message"""

    """loop to enter data into the calculation dictionary"""
    for key1 in winPossibility:
        for key2 in winPossibility[key1]:
            if key2 == int(position):
                winPossibility[key1][key2] = symbl

    """loop to determine winner in the calculation dictionary"""
    for key in winPossibility:
        if list(winPossibility[key].values()).count(symbl) == 3:
            print(list(winPossibility[1].values()).count(symbl))
            print("Game Over!!!")
            return player


# Start
player1, player2 = userNameInput(symbl1, symbl2)

"""Instructions for players"""
print("\nBelow Matrix shows the tic tac toe positions for the game.\n"
      "Players will be able to put value ('X' or 'O') by selecting any number between 1-9 which will determine the\n"
      "position in the matrix as shown below.\n")
print("Matrix".center(10, '*'))
print("{} | {} | {}".format(1, 2, 3))
print("- - - - -")
print("{} | {} | {}".format(4, 5, 6))
print("- - - - -")
print("{} | {} | {}".format(7, 8, 9))

exhst = 0

while True:
    """loop to run through the matrix"""

    winner = playerMove(player1, symbl1)
    exhst = exhst + 1
    if winner == player1:
        print("\nCongratulations {}, you WON !!!".format(player1))
        break

    if exhst == 9:
        print("\nIt's a Draw..!")
        break

    winner = playerMove(player2, symbl2)
    exhst = exhst + 1
    if winner == player2:
        print("\nCongratulations {}, you WON !!!".format(player2))
        break

    if exhst == 9:
        print("\nIt's a Draw..!")
        break
