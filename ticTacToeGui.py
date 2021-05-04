# Tic Tac Toe GUI with guizero
# James Taddei
# 5/3/21

# Current goal: refactor in a single loop that creates all of the
# buttons then use a number to grid converter. Afterwards, add in
# the actual code behind the rest of tic tac toe.

# The way that this works is that you need to set the button's
# text to 'X' or 'O' (buttonName.text = "X"). Since these buttons
# all have the same name though and are stored in the list, we use
# currBoard[pos].text = "X" instead.

# For this specific script, it creates 9 buttons and adds them
# to current board. Whenever they're pressed, the text in them
# is changed to "X". Code needs a lot of refactoring, then try to
# import code from the text version.

import guizero as gui

def grid_to_num(x, y):
  """
  Takes x and y as inputs and returns a 
  1-9 position number
  """

  total = (3 * x) + y
  return total

def button_press(x, y, currBoard):
  """
  Adds the players symbol to the button
  that they pressed
  """

  addSymbol = "X"

  numPos = grid_to_num(x, y)
  currBoard[numPos].text = addSymbol

  # Setting text color
  if (addSymbol == "X"):
    currBoard[numPos].text_color = "#3ffc0a"
  elif (addSymbol == "O"):
    currBoard[numPos].text_color = "#f505e5"

  print(currBoard[numPos].text + "O")

def main():
  global currBoard
  currBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

  # Window creation
  global app
  app = gui.App(title="Tic Tace Toe")
  app.bg = "black"

  # Text creation
  message = gui.Text(app, text="Welcome to the app")
  message.text_color = "white"

  # Board Creation
  gameBoard = gui.Box(app, layout="grid")

  # Buttons
  for x in range(3):
    for y in range(3):
      buttonText = currBoard[grid_to_num(x, y)]
      button = gui.PushButton(gameBoard, command=button_press, args=[x, y, currBoard], text=buttonText, grid=[x, y], width=3)

      currBoard[grid_to_num(x, y)] = button

  # Displaying the app
  app.display()

main()