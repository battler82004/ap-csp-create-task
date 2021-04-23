# Tic Tac Toe
# James Taddei
# 4/22/21

""" Need:
Upload current version to github
Refactor
Comment
F-strings for functions

GUI
"""

import random
from time import sleep

def main():
    # User input for the number of players
    try:
        numOfPlayers = int(raw_input("Enter the number of players (one or two): "))
    except:
        print("Please enter either '1' or '2'")
        return(main())
        
    # Sends the program to play the game based on the number of players
    if (numOfPlayers == 0): # Has two bots play against each other
        currBoard = two_bots_game()
    elif (numOfPlayers == 1): # Has the player and bot play against each other
        playerTurnNum = find_turn_order() # Has the player pick if they go first
        if (playerTurnNum == 1):
            currBoard = player_first_game()
        else:
            currBoard = bot_first_game()
    elif (numOfPlayers == 2): # Has two players play against each other
        currBoard = two_player_game()
    else: # Restarts if there's an invalid number of players
        print("Please enter either '1' or '2'")
        return(main())
        
    # Checks if someone has won and if so who won
    # Should be refactored with just the win checker loop I made
    if (win_checker(currBoard)):
        # Finds the winnner
        locationsToCheck = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]] # All ways to win
        for i in range(8): # Finds the symbol in the winning positions
            pos1, pos2, pos3 = locationsToCheck[i]
            if ((currBoard[pos1] == currBoard[pos2]) and (currBoard[pos2] == currBoard[pos3]) and (currBoard[pos1] != "  ")):
                winner = currBoard[pos1]
                
        # Returns the win message
        if (winner == "X"): # Player / Player 1 / Bot 1 win return
            if (numOfPlayers == 1): # Player win vs Bot
                return ("\n\nYou have triumphed over the bot! Congratulations on the victory!")
            elif (numOfPlayers == 2): # Player 1 win vs Player 2
                return ("\n\nCongratulations on your victory against your opponent!")
            else: # Bot 1 win
                return ("\n\nBot number 1 has run the epic battle against the other bot!")
        elif (winner == "O"): # Bot / Player 2 / Bot 2 win return
            if (numOfPlayers == 1): # Bot win vs Player
                return ("\n\nThe bot has bested you! Better luck next time.")
            elif (numOfPlayers == 2): # Player 2 win vs Player 1
                return ("\n\nCongratulations on your victory against your opponent!")
            else: # Bot 2 win
                return ("\n\nBot number 2 rules the day after defeating the other bot!")
    else: # Retuns a draw message
        if (numOfPlayers == 1): # Draw in Player vs Bot
            return ("You have tied with the bot. Kind of anticlimactic. Hopefully you'll win next time.")
        elif (numOfPlayers == 2): # Draw in Player vs Player
            return ("You have tied with each other. Kind of anticlimactic. Hopefully someone will win next time.")
        else: # Draw in Bot vs Bot
            return ("The bots have tied with each other. Kind of anticlimactic. Hopefully one will win next time.")
        
def two_bots_game():
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        
    # Main turn loop
    while not(win_checker(currBoard)):
        # Bot 1's turn
        currBoard = bot_turn(currBoard, "X", "O")
        board_printer(currBoard)
        if (win_checker(currBoard) or tie_checker(currBoard)):
            break
            
        # Waits 2 seconds before bot 2's turn
        sleep(2)
            
        # Bot 2's turn
        currBoard = bot_turn(currBoard, "O", "X")
        board_printer(currBoard)
        if (tie_checker(currBoard)):
            break
        
    return currBoard
        
def player_first_game():
    before_first_turn()
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        
    # Main turn loop
    while not(win_checker(currBoard)):
        # Player 1's turn
        try: # Location Input
            playerTurnLocation = int(raw_input(("Location to place 'X': ")))
            playerTurnLocation -= 1
        except:
            print("Please enter either '1' or '2'")
            continue
                
        # Checks if the move is valid
        if not(valid_location(currBoard, playerTurnLocation)):
            if (playerTurnLocation > 8 or playerTurnLocation < 0):
                print("Error, number should be from 1-9")
            elif (currBoard[playerTurnLocation] != "  "):
                print("Error, something is already there")
            continue
                
        # Actually adds the player's move
        currBoard[playerTurnLocation] = "X"
        board_printer(currBoard)
        if (win_checker(currBoard) or tie_checker(currBoard)):
            break
            
        # Bot's turn
        currBoard = bot_turn(currBoard, "X", "O")
        board_printer(currBoard)
        if (tie_checker(currBoard)):
            break
        
    return currBoard
    
def bot_first_game():
    before_first_turn()
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
    isPlayersTurn = False
    
    # Main turn loop
    while not(win_checker(currBoard)):
        if not(isPlayersTurn): # Checks if the player is meant to go next
            # Bot's turn
            currBoard = bot_turn(currBoard, "X", "O")
            board_printer(currBoard)
            if (win_checker(currBoard) or tie_checker(currBoard)):
                break
            
        # Player's turn
        try: # Location Input
            playerTurnLocation = int(raw_input(("Location to place 'X': ")))
            playerTurnLocation -= 1
        except:
            print("Please enter either '1' or '2'")
            isPlayersTurn = True
            continue
                
        # Checks if the move is valid
        if not(valid_location(currBoard, playerTurnLocation)):
            if (playerTurnLocation > 8 or playerTurnLocation < 0):
                print("Error, number should be from 1-9")
            elif (currBoard[playerTurnLocation] != "  "):
                print("Error, something is already there")
            isPlayersTurn = True
            continue
                
        # Actually adds the player's move
        isPlayersTurn = False
        currBoard[playerTurnLocation] = "X"
        board_printer(currBoard)
        if (tie_checker(currBoard)):
            break
            
    return currBoard
        
def two_player_game():
    before_first_turn()
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
    playerTwosTurn = False
    
    # Main turn loop
    while not(win_checker(currBoard)):
        # Player 1's turn
        if not(playerTwosTurn): # Checks if player two still needs to go
            try: # Location Input
                playerTurnLocation = int(raw_input(("Location to place 'X': ")))
                playerTurnLocation -= 1
            except:
                print("Please enter either '1' or '2'")
                continue
                
            # Checks if the move is valid
            if not(valid_location(currBoard, playerTurnLocation)):
                if (playerTurnLocation > 8 or playerTurnLocation < 0):
                    print("Error, number should be from 1-9")
                elif (currBoard[playerTurnLocation] != "  "):
                    print("Error, something is already there")
                continue
                
            # Actually adds the player's move
            currBoard[playerTurnLocation] = "X"
            board_printer(currBoard)
            if (win_checker(currBoard) or tie_checker(currBoard)):
                break
            
        # Player 2's turn
        try: # Location Input
            playerTurnLocation = int(raw_input(("Location to place 'O': ")))
            playerTurnLocation -= 1
        except:
            print("Please enter a number (i.e. '5')")
            playerTwosTurn = True
            continue
                
        # Checks if the move is valid
        if not(valid_location(currBoard, playerTurnLocation)):
            if (playerTurnLocation > 8 or playerTurnLocation < 0):
                print("Error, number should be from 1-9")
            elif (currBoard[playerTurnLocation] != "  "):
                print("Error, something is already there")
            playerTwosTurn = True
            continue
                
        # Actually adds the player's move
        playerTwosTurn = False
        currBoard[playerTurnLocation] = "O"
        board_printer(currBoard)
        if (tie_checker(currBoard)):
            break
        
    return(currBoard)
    
def find_turn_order():
    try: # Tries to have the user input a number
        playerTurnNum = int(raw_input("Input a '1' to go first or a '2' to go second: "))
    except: # Asks the user to input '1' or '2'
        print("Error, please enter either '1' or '2'.")
        return find_turn_order()
    
    if (playerTurnNum == 1 or playerTurnNum == 2): # Checks that the number is 1 or 2
        return playerTurnNum
    else: # Asks the user to input '1' or '2'
        print("Error, please enteer either '1' or '2'.")
        return find_turn_order()
    
def before_first_turn():
    print("\nTo select the location of where you'll be placing your 'X', enter")
    print("the number corresponding to the positon on the board below\n")
    board_printer(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    
def win_checker(currBoard):
   # This var is all of the locations that need to be checked to look over the 8 possible ways to win
   # 8 checks - 3 vertical, 3 horizontal, 2 crosses
    locationsToCheck = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    
    # Checks if any win condition is true
    for i in range(8):
        pos1, pos2, pos3 = locationsToCheck[i]
        # If someone has 3 in a row, then Trueis returned
        if ((currBoard[pos1] == currBoard[pos2]) and (currBoard[pos2] == currBoard[pos3]) and (currBoard[pos1] != "  ")):
            return True

    # Final return statement which says that no one has won
    return False
	
def valid_location(currBoard, location):
    if (location > 8 or location < 0):
        return False
    elif (currBoard[location] != "  "):
        return False
    else:
        return True
    
def board_printer(currBoard):
    print("\n  " + currBoard[0] + " | " + currBoard[1] + " | " + currBoard[2])
    print("------------")
    print("  " + currBoard[3] + " | " + currBoard[4] + " | " + currBoard[5])
    print("------------")
    print("  " + currBoard[6] + " | " + currBoard[7] + " | " + currBoard[8])
    
def tie_checker(currBoard):
    # Finds how many squares are filled in
    filledInCount = 0
    for pos in currBoard:
        if (pos != "  "):
            filledInCount += 1
            
    # Checks if all the squares are filled (if there's a tie)
    if (filledInCount == 9):
        return True
    else:
        return False
        
def bot_turn(currBoard, opponentSymbol, friendlySymbol):
    squaresToProtect = places_to_win(currBoard, opponentSymbol)
    
    # Finds where to place the bot's 'O' for this turn
    if (len(squaresToProtect) >= 1): # Checks if there's a way the enemy can win
        if (random.randint(0, 3) == 0): # Has a 3/4 chance to protect where the enemy can win
            toPlace = random_location(currBoard) # Picks a random location to place the 'O'
        else: # Chooses the protecting option
            toPlace = squaresToProtect[0]
    else: # Since there's nowhere to proteect, the bot chooses a random spot
        toPlace = random_location(currBoard)
        
    # Adds the move to the board
    currBoard[toPlace] = friendlySymbol
    
    return currBoard

def places_to_win(currBoard, checkingFor):
    def win_pos_finder(posChecking):
        if (currBoard[posChecking[0]] == currBoard[posChecking[1]] and currBoard[posChecking[0]] == checkingFor and currBoard[posChecking[2]] == "  "):
            return posChecking[2] # Returns the 3rd element if that position is where the player could win
	elif (currBoard[posChecking[1]] == currBoard[posChecking[2]] and currBoard[posChecking[1]] == checkingFor and currBoard[posChecking[0]] == "  "):
	    return posChecking[0] # Returns the 1st element if that position is where the player could win
	elif (currBoard[posChecking[0]] == currBoard[posChecking[2]] and currBoard[posChecking[0]] == checkingFor and currBoard[posChecking[1]] == "  "):
	    return posChecking[1] # Returns the 2nd element if that position is where the player could win
	else:
	    return 10 # Returns 10 if there is no position where the player could win (for this specific way to win)
    
    locationsToCheck = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    posToBlockWin = []
    
    # Removes 10's (placeholders) from the list of positions to block
    for i in range(8):
        potentialLocation = win_pos_finder(locationsToCheck[i])
        if (potentialLocation != 10):
            posToBlockWin.append(potentialLocation)
        
    return posToBlockWin
    
def random_location(currBoard):
    location = random.randint(0, 8)
    while not(valid_location(currBoard, location)): # Checks if the move is valid
            location = random.randint(0, 8)
    
    return location
    
print(main())