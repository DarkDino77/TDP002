#create the begining board
def create_board():
    return [['player',1,1]]
#Adding the difrent things to the board
def add_to_board(board, x, y, unit):
    pass
def add_wall(board, x, y):
    add_to_board(board, x, y, "wall")
def add_box(board, x, y):
    add_to_board(board, x, y, "box")
def add_storage(board, x, y):
    add_to_board(board, x, y, "storage")
#
# Display board
#
# cheack a cordinate on the board
#
# move player
# Make your move (a)left, (d)right, (w)up, (s)down: l
#
# cheack collision with player
#
# move box
#
# read file 
#
# convert file.txt to board
#
# chose a level
#
# play game 
#
# victory massage 
#

board = create_board()
print(board)