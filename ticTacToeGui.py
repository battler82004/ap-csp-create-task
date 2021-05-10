# Tic Tac Toe GUI with guizero
# James Taddei
# 5/10/21

""" Need:
Finish functionality
Test
Refactor, comment, and f-strings
Upload to github
"""

# The way that this works is that you need to set the button's
# text to 'X' or 'O' (buttonName.text = "X"). Since these buttons
# all have the same name though and are stored in the list, we use
# currBoard[pos].text = "X" instead.

import guizero as gui
from math import floor
from random import randint
from time import sleep

def num_to_grid(gridNum):
  """
  Takes a grid number (1-9) and returns the number as
  a grid array (x, y)
  """

  x = gridNum % 3
  y = floor(gridNum / 3)
  return (x, y)

def valid_location(currBoard, location):
    """
    Takes in the current board and a potential location and checks if placing
    something in that square is a valid move or not. Ends by returning true
    if the move's valid and false otherwise.
    """
    
    if (currBoard[location].text != " "): # Checks if the location is taken
        return False
    else:
        return True

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
        if ((currBoard[pos1].text == currBoard[pos2].text) and (currBoard[pos2].text == currBoard[pos3].text) and (currBoard[pos1].text != " ")):
            return (True, currBoard[pos1].text)

    # Final return statement which says that no one has won
    return (False, "none")

def tie_checker(currBoard):
    """
    Takes in the current board and checks if there's a tie. To check for a tie,
    the script searches for whether or not the board is filled. Returns true
    if the board is filled and false if not.
    """
    
    # Finds how many squares are filled in
    filledInCount = 0
    for pos in currBoard:
        if (pos.text != " "):
            filledInCount += 1
            
    # Checks if all the squares are filled (if there's a tie)
    if (filledInCount == 9):
        return True
    else:
        return False

def flip_symbol(symbol):
  """
  Takes in the symbol of the current player and flips it
  """
  global currSymbol
  if (symbol == "X"):
    currSymbol = "O"
  else:
    currSymbol = "X"

def is_game_over():
  """
  Checks if the game is over and calls the final print function
  if it is.
  """

  if ((win_checker(currBoard))[0] or tie_checker(currBoard)):
    return (final_printer(currBoard, 2))
  else:
    return 0

def places_to_win(currBoard, checkingFor):
  """
  Takes in the current board and the enemy's symbol and checks if
  the enemy can win next turn (has 2 in a row with an empty space
  after). All of the positions where the enemy could win next turn
  are then returned.
  """
    
  def win_pos_finder(posChecking):
    """
    Takes in a list of 3 positions that would allow someone to win
    and checks if the enemy has 2/3 of them. If this is the case, the
    potential win position is returned. Otherwise, 10 is returned as 
    a placeholder.
    """
        
    if (currBoard[posChecking[0]].text == currBoard[posChecking[1]].text and currBoard[posChecking[0]].text == checkingFor and currBoard[posChecking[2]].text == "  "):
      return posChecking[2] # Returns the 3rd element if that position is where the player could win
    elif (currBoard[posChecking[1]].text == currBoard[posChecking[2]].text and currBoard[posChecking[1]].text == checkingFor and currBoard[posChecking[0]].text == "  "):
        return posChecking[0] # Returns the 1st element if that position is where the player could win
    elif (currBoard[posChecking[0]].text == currBoard[posChecking[2]].text and currBoard[posChecking[0]].text == checkingFor and currBoard[posChecking[1]].text == "  "):
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
  Chooses a random valid location for the bot to place its 'X' or 'O'
  this turn. This location is then returned.
  """
    
  location = randint(0, 8)
  while not(valid_location(currBoard, location)): # Checks if the move is valid
    location = randint(0, 8)
    
  return location

def bot_turn(opponentSymbol, friendlySymbol):
  """
  Takes the current board, the enemy's symbol (like 'X'), and the
  friendly symbol (like 'O'). It then has the bot 'choose' a
  position and place its symbol there before printing the new
  board. It ends by returning the current board.
  """

  if (win_checker(currBoard)[0] or tie_checker(currBoard)):
    return

  squaresToProtect = places_to_win(currBoard, opponentSymbol)
    
  # Finds where to place the bot's 'O' for this turn
  if (len(squaresToProtect) >= 1): # Checks if there's a way the enemy can win
    if (randint(0, 2) == 0): # Has a 2/3 chance to protect where the enemy can win
      toPlace = random_location(currBoard) # Picks a random location to place the 'O'
    else: # Chooses the protecting option
      toPlace = squaresToProtect[0]
  else: # Since there's nowhere to proteect, the bot chooses a random spot
    toPlace = random_location(currBoard)

  # Adds the move to the board and prints the new board
  currBoard[toPlace].text = friendlySymbol

  if (currSymbol == "X"):
    currBoard[toPlace].text_color = "#3ffc0a"
  elif (currSymbol == "O"):
    currBoard[toPlace].text_color = "#f505e5"

  flip_symbol(currSymbol)
  is_game_over()

def reset_symbol():
  global currSymbol
  currSymbol = "X"

def who_is_first(whoIsFirst):
  orderSelector.visible = False

  global botNeedsTurn

  if (whoIsFirst == 1):
    creatorInfo = ("X", "player_first")
    botNeedsTurn = False
  else:
    creatorInfo = ("O", "bot_first")
    botNeedsTurn = True

  newInstructionalMessage.visible = False
  game_creator(creatorInfo[0], creatorInfo[1])

def num_players_selector(x):
  numOfPlayersBoard.visible = False
  instructionMessage.visible = False

  if (x == 1):
    # Instructional text
    global newInstructionalMessage
    newInstructionalMessage = gui.Text(app, color = "white", text= "\nClick '1' to go first or '2' to go second")

    global orderSelector
    orderSelector = gui.Box(app, layout="grid")

    for x in range(1, 3):
      button = gui.PushButton(orderSelector, command=who_is_first, args=[x], text=str(x), grid=[x, 0], width=5, height=3)
      button.text_color = "green"

  elif (x == 2):
    game_creator("X", "two_players")
  else: # game_creator with it working
    game_creator("X", "two_bots")

def main():
  # Window creation
  global app
  app = gui.App(title="Tic Tace Toe")
  app.bg = "black"

  # Instructional text
  global instructionMessage
  instructionMessage = gui.Text(app, color = "white", text="\nSelect the number of players")

  # Board Creation
  global numOfPlayersBoard
  numOfPlayersBoard = gui.Box(app, layout="grid")

  # Button creation
  for x in range(3):
    button = gui.PushButton(numOfPlayersBoard, command=num_players_selector, args=[x], text=str(x), grid=[x, 0], width=5, height=3)
    button.text_color = "green"

  # Displaying the app
  app.display()

def two_bots_button(pos, currBoard):
  if (not(win_checker(currBoard)[0]) and not(tie_checker(currBoard))):
    while True:
      if (currSymbol == "X"):
        bot_turn("X", "O")
      else:
        bot_turn("O", "X")

      isGameOver = is_game_over()
      if (isGameOver != 0):
        print(isGameOver)
        break
        
      sleep(0.5)

  else:
    # Game reset
    for i in range(9):
      currBoard[i].text = " "
    reset_symbol()

def one_player_button(pos, currBoard, botIsFirst):
  """
  Adds the players symbol to the button
  that they pressed.
  """

  if (not(win_checker(currBoard)[0]) and not(tie_checker(currBoard))):
    if (valid_location(currBoard, pos)):
      currBoard[pos].text = currSymbol
      errorMessage.value = ""
    else:
      errorMessage.value = "Error, please click on a square that isn't taken already"
      return

    # Setting text color
    if (currSymbol == "X"):
      currBoard[pos].text_color = "#3ffc0a"
    elif (currSymbol == "O"):
      currBoard[pos].text_color = "#f505e5"
    
    isGameOver = is_game_over()
    if (isGameOver != 0):
      print(isGameOver)
      return

    flip_symbol(currSymbol)
    if (currSymbol == "O"):
      bot_turn("X", "O")

    isGameOver = is_game_over()
    if (isGameOver != 0):
      print(isGameOver)

  else:
    # Game reset
    for i in range(9):
      currBoard[i].text = " "
    reset_symbol()

    if (botIsFirst):
      sleep(0.5)
      bot_turn("X", "O")

      for i in range(9):
        if (currBoard[i].text == "O"):
          currBoard[i].text_color = "#f505e5"

      flip_symbol(currSymbol)

def two_players_button(pos, currBoard):
  """
  Adds the players symbol to the button
  that they pressed.
  """

  if (not(win_checker(currBoard)[0]) and not(tie_checker(currBoard))):
    if (valid_location(currBoard, pos)):
      currBoard[pos].text = currSymbol
      errorMessage.value = ""
    else:
      errorMessage.value = "Error, please click on a square that isn't taken already"
      return

    # Setting text color
    if (currSymbol == "X"):
      currBoard[pos].text_color = "#3ffc0a"
    elif (currSymbol == "O"):
      currBoard[pos].text_color = "#f505e5"
    
    isGameOver = is_game_over()
    if (isGameOver != 0):
      print(isGameOver)
      return

    flip_symbol(currSymbol)

  else:
    # Game reset
    for i in range(9):
      currBoard[i].text = " "
    reset_symbol()

def button_press(pos, currBoard, buttonPressFunc):
  if (buttonPressFunc == "two_bots"):
    two_bots_button(pos, currBoard)
  elif (buttonPressFunc == "player_first"):
    one_player_button(pos, currBoard, False)
  elif (buttonPressFunc == "bot_first"):
    one_player_button(pos, currBoard, True)
  else:
    two_players_button(pos, currBoard)

def game_creator(startSymbol, buttonPressFunc):
  """
  This function will create the board and set up the screen
  for the actual game.
  """

  global currBoard, currSymbol
  currBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
  currSymbol = startSymbol

  # Board Creation
  gameBoard = gui.Box(app, layout="grid")

  # Button creation
  for pos in range(9):
    buttonText = currBoard[pos]
    x, y = num_to_grid(pos)
    button = gui.PushButton(gameBoard, command=button_press, args=[pos, currBoard, buttonPressFunc], text=buttonText, grid=[x, y], width=3)

    currBoard[pos] = button

  # Instructional text
  global userPrompt, errorMessage
  userPrompt = gui.Text(app, color="white", text="Click on an open square to place your symbol there")
  errorMessage = gui.Text(app, color = "red", text="")

  if (buttonPressFunc == "bot_first"):
    bot_turn("X", "O")

def final_printer(currBoard, numOfPlayers):
  """
  Prints out a message based on who won
  """

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
      return ("\n\nYou have tied with the bot. Kind of anticlimactic. Hopefully you'll win next time.")
    elif (numOfPlayers == 2): # Draw in Player vs Player
      return ("\n\nYou have tied with each other. Kind of anticlimactic. Hopefully someone will win next time.")
    else: # Draw in Bot vs Bot
      return ("\n\nThe bots have tied with each other. Kind of anticlimactic. Hopefully one will win next time.")

main()
