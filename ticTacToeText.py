# Tic Tac Toe
# James Taddei
# 4/26/21

""" Need:
GUI
"""

import random
from time import sleep

def main():
    """
    Has the user play a game of tic tac toe against another player or a bot. Returns
    a relevant win/draw message at the end.
    """
    
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
    anyoneWon, winner = win_checker(currBoard)
    if (anyoneWon):     
        # Returns the win message
        if (winner == "X"): # Player / Player 1 / Bot 1 win return
            if (numOfPlayers == 1): # Player win vs Bot
                return ("\n\nYou have triumphed over the bot! Congratulations on the victory!")
            elif (numOfPlayers == 2): # Player 1 win vs Player 2
                return ("\n\nCongratulations player 1 on your victory against your opponent!")
            else: # Bot 1 win
                return ("\n\nBot number 1 has won the epic battle against the other bot!")
        elif (winner == "O"): # Bot / Player 2 / Bot 2 win return
            if (numOfPlayers == 1): # Bot win vs Player
                return ("\n\nThe bot has bested you! Better luck next time.")
            elif (numOfPlayers == 2): # Player 2 win vs Player 1
                return ("\n\nCongratulations player 2 on your victory against your opponent!")
            else: # Bot 2 win
                return ("\n\nBot number 2 rules the day after defeating bot 1!")
    else: # Retuns a draw message
        if (numOfPlayers == 1): # Draw in Player vs Bot
            return ("You have tied with the bot. Kind of anticlimactic. Hopefully you'll win next time.")
        elif (numOfPlayers == 2): # Draw in Player vs Player
            return ("You have tied with each other. Kind of anticlimactic. Hopefully someone will win next time.")
        else: # Draw in Bot vs Bot
            return ("The bots have tied with each other. Kind of anticlimactic. Hopefully one will win next time.")
        
def two_bots_game():
    """
    Has two bots play tic tac toe against eachother then returns the final board.
    """
    
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        
    # Main turn loop
    while True:
        # Bot 1's turn
        currBoard = bot_turn(currBoard, "O", "X")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
            
        # Waits 2 seconds before bot 2's turn
        sleep(2)
            
        # Bot 2's turn
        currBoard = bot_turn(currBoard, "X", "O")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
                
    return currBoard
        
def player_first_game():
    """
    Has the user play tic tac toe against the bot (going first). Ends by returning
    the final board.
    """
    
    before_first_turn()
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        
    # Main turn loop
    while True:
        # Player's turn
        currBoard = full_player_turn(currBoard, "X")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
            
        # Bot's turn
        currBoard = bot_turn(currBoard, "X", "O")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
        
    return currBoard
    
def bot_first_game():
    """
    Has the user play tic tac toe against the bot (going second). Ends by returning
    the final board.
    """
    
    before_first_turn()
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
    
    # Main turn loop
    while True:
        # Bot's turn
        currBoard = bot_turn(currBoard, "X", "O")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
            
        # Player's turn
        currBoard = full_player_turn(currBoard, "X")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
            
    return currBoard
        
def two_player_game():
    """
    Has two users play tic tac toe against each other. Ends by returning the final
    board.
    """
    
    before_first_turn()
    currBoard = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
    
    # Main turn loop
    while True:
        # Player 1's turn
        currBoard = full_player_turn(currBoard, "X")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
            
        # Player 2's turn
        currBoard = full_player_turn(currBoard, "O")
        if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
            break
        
    return(currBoard)
    
def find_turn_order():
    """
    Has the users pick whether they'd like to go first or second against the bot
    and returns whether they'd like to go first or not.
    """
    
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
    """
    Prints to the user some basic instructions on how they'll pick where to place
    their 'X' or 'O'.
    """
    
    print("\nTo select the location of where you'll be placing your 'X', enter")
    print("the number corresponding to the positon on the board below\n")
    board_printer(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    
def win_checker(currBoard):
    """
    Takes in the current board, finds whether or not someone can win
    and who wins, and returns a tuple with these two parts.
    """
    
   # This var is all of the locations that need to be checked to look over the 8 possible ways to win
   # 8 checks - 3 vertical, 3 horizontal, 2 crosses
    locationsToCheck = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    
    # Checks if any win condition is true
    for i in range(8):
        pos1, pos2, pos3 = locationsToCheck[i]
        # If someone has 3 in a row, then True is returned
        if ((currBoard[pos1] == currBoard[pos2]) and (currBoard[pos2] == currBoard[pos3]) and (currBoard[pos1] != "  ")):
            return (True, currBoard[pos1])

    # Final return statement which says that no one has won
    return (False, "none")
	
def valid_location(currBoard, location):
    """
    Takes in the current board and a potential location and checks if placing
    something in that square is a valid move or not. Ends by returning true
    if the move's valid and false otherwise.
    """
    
    if (location > 8 or location < 0): # Checks if the number is too small or big
        return False
    elif (currBoard[location] != "  "): # Checks if the location is taken
        return False
    else:
        return True
    
def board_printer(currBoard):
    """
    Takes the current board and prints it out to the user.
    """
    
    print("\n  " + currBoard[0] + " | " + currBoard[1] + " | " + currBoard[2])
    print("------------")
    print("  " + currBoard[3] + " | " + currBoard[4] + " | " + currBoard[5])
    print("------------")
    print("  " + currBoard[6] + " | " + currBoard[7] + " | " + currBoard[8])
    
def tie_checker(currBoard):
    """
    Takes in the current board and checks if there's a tie. To check for a tie,
    the script searches for whether or not the board is filled. Returns true
    if the board is filled and false if not.
    """
    
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
    """
    Takes the current board, the enemy's symbol (like 'X'), and the friendly
    symbol (like 'O'). It then has the bot 'choose' a position and place its symbol
    there before printing the new board. It ends by returning the current board.
    """
    
    squaresToProtect = places_to_win(currBoard, opponentSymbol)
    
    # Finds where to place the bot's 'O' for this turn
    if (len(squaresToProtect) >= 1): # Checks if there's a way the enemy can win
        if (random.randint(0, 2) == 0): # Has a 2/3 chance to protect where the enemy can win
            toPlace = random_location(currBoard) # Picks a random location to place the 'O'
        else: # Chooses the protecting option
            toPlace = squaresToProtect[0]
    else: # Since there's nowhere to proteect, the bot chooses a random spot
        toPlace = random_location(currBoard)
        
    # Adds the move to the board and prints the new board
    currBoard[toPlace] = friendlySymbol
    board_printer(currBoard)
    
    return currBoard

def places_to_win(currBoard, checkingFor):
    """
    Takes in the current board and the enemy's symbol and checks if the enemy
    can win next turn (has 2 in a row with an empty space after). All of the
    positions where the enemy could win next turn are then returned.
    """
    
    def win_pos_finder(posChecking):
        """
        Takes in a list of 3 positions that would allow someone to win and checks
        if the enemy has 2/3 of them. If this is the case, the potential win position
        is returned. Otherwise, 10 is returned as a placeholder.
        """
        
        if (currBoard[posChecking[0]] == currBoard[posChecking[1]] and currBoard[posChecking[0]] == checkingFor and currBoard[posChecking[2]] == "  "):
            return posChecking[2] # Returns the 3rd element if that position is where the player could win
	elif (currBoard[posChecking[1]] == currBoard[posChecking[2]] and currBoard[posChecking[1]] == checkingFor and currBoard[posChecking[0]] == "  "):
	    return posChecking[0] # Returns the 1st element if that position is where the player could win
	elif (currBoard[posChecking[0]] == currBoard[posChecking[2]] and currBoard[posChecking[0]] == checkingFor and currBoard[posChecking[1]] == "  "):
	    return posChecking[1] # Returns the 2nd element if that position is where the player could win
	else:
	    return 10 # Returns 10 if there is no position where the player could win (for this specific way to win)
    
    locationsToCheck = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]] # List of all of the ways to win
    posToBlockWin = []
    
    # Removes 10's (placeholders) from the list of positions to block
    for i in range(8):
        potentialLocation = win_pos_finder(locationsToCheck[i])
        if (potentialLocation != 10):
            posToBlockWin.append(potentialLocation)
        
    return posToBlockWin # A list of all of the places where the enemy could win next turn
    
def random_location(currBoard):
    """
    Chooses a random valid location for the bot to place its 'X' or 'O' this turn.
    This location is then returned.
    """
    
    location = random.randint(0, 8)
    while not(valid_location(currBoard, location)): # Checks if the move is valid
            location = random.randint(0, 8)
    
    return location
    
def full_player_turn(currBoard, symbol):
    """
    Takes in the current board and the player's symbol and has them go through
    a full turn. This includes inputting a location, checking its validity, adding the
    player's move, and printing the new board. This ends when the new current
    board is returned.
    """
    
    try: # Location Input
            playerTurnLocation = int(raw_input(("Location to place '" + symbol + "': ")))
            playerTurnLocation -= 1
    except:
        print("Please enter  a number like '6'")
        return(full_player_turn(currBoard, symbol))
                
    # Checks if the move is valid
    if not(valid_location(currBoard, playerTurnLocation)):
        if (playerTurnLocation > 8 or playerTurnLocation < 0):
            print("Error, number should be from 1-9")
        elif (currBoard[playerTurnLocation] != "  "):
            print("Error, something is already there")
        return(full_player_turn(currBoard, symbol))
                
    # Actually adds the player's move
    currBoard[playerTurnLocation] = symbol
    board_printer(currBoard)
    
    return currBoard
    
print(main())
