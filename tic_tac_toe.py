"""
Tic Tac Toe Game 
@author: Gabby Clavell 

This program is designed to have two players play tic tac toe. It takes one argument, from 1-9, and writes their input into the board. 
The board is indexed from 1-9 as the board is 3x3 and 1-3 represent the first row, 4-6 represent the second row, and 7-9 represent the 
last row. If the user gives a wrong input, the program will keep requesting a new position until it is correct. If the position given 
is taken already, it keeps asking for a new position until there is an empty slot given. 
"""

# -------- Global Variables --------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"

# -------- Functions --------

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#Play the game!
def play_game():
    
    #first display the board 
    display_board()

    while game_still_going:

        #handle the turn
        handle_turn(current_player)

        #check to see if the game is over 
        game_over()

        #move onto the next player 
        flip_player()

    if winner == 'X' or winner == 'O':
        print(winner + 'wins!')
    else:
        print('Tie!')

def check_for_winner():

  #set global vars
  global winner 
  #check rows
  row_winner = check_rows()
  #check columns
  col_winner = check_cols()
  #check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    #there is a winner
    winner = row_winner

  elif col_winner:
    #winner 
    winner = col_winner
  elif diagonal_winner:
    winner = diagonal_winner
    #winner
  else:
    #no winner
    winner == None
  return 

def check_rows():
  #set global vars 
  global game_still_going

  #check if any rows have all same val and not empty
  row_1 = board[0] == board[1] == board[2] != '-'
  row_2 = board[3] == board[4] == board[5] != '-'
  row_3 = board[6] == board[7] == board[8] != '-'

  #if any row has a match, flag there is a win 
  if row_1 or row_2 or row_3:
    game_still_going = False

    #return the winner X or O
    if row_1:
      return board[0]
    elif row_2:
      return board[3]
    elif row_3:
      return board[6]
  return 

def check_cols():
  #set global vars 
  global game_still_going

  #check if any rows have all same val and not empty
  col_1 = board[0] == board[3] == board[6] != '-'
  col_2 = board[1] == board[4] == board[7] != '-'
  col_3 = board[2] == board[5] == board[8] != '-'

  #if any row has a match, flag there is a win 
  if col_1 or col_2 or col_3:
    game_still_going = False

    #return the winner X or O
    if col_1:
      return board[0]
    elif col_2:
      return board[1]
    elif col_3:
      return board[2]
  return 

def check_diagonals():
  #set global vars 
  global game_still_going

  #check if any rows have all same val and not empty
  diag_1 = board[0] == board[4] == board[8] != '-'
  diag_2 = board[2] == board[4] == board[6] != '-'

  #if any row has a match, flag there is a win 
  if diag_1 or diag_2:
    game_still_going = False
    return board[4]

    #return the winner X or O
    #if diag_1 or diag_2:
      #return board[4]
  return 

def check_if_tie():

  global game_still_going

  if '-' not in board:
    game_still_going = False
  return 

def flip_player():
  #global vars needed to set up 
  global current_player

  #if current_player is X, change to O
  if current_player == 'X':
    current_player = 'O'
  #if current_player is O then change to X
  else:
    current_player = 'X'

def game_over():
  check_for_winner()
  check_if_tie()

#handle a single turn of a player
def handle_turn(player):

  #put who's turn it is
  print(player + "'s turn!")

  #valid input for number range and if the spot was not taken
  #used for while loop
  valid = False

  #get a position from the user - minus one for indexing reasons
  position = input('Choose a position from 1-9: ')
  #check to see if the input is in this list 
  number_range = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

  #stay in loop until the input is valid!
  while not valid:
    while position not in number_range:
      position = input('Choose a position from 1-9: ')
    
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("That position is taken. Try again.")


  board[position] = player

  display_board()


# -------- Start Program --------
play_game()
play_again = True

while play_again:

  ans = input('Want to play again? ')

  while ans not in ['yes', 'no']:
    ans = input('Want to play again? ')

  if ans == 'yes':
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
    game_still_going = True
    winner = None
    current_player = "X"
    play_game()
  else:
    play_again = False


