#create the begining board
# The board is a list of items where it stores secondary list of tuples
# where the secondary list position in the first list is the y cordinate
# And the tuple has the x and peice information 
def create_board():
    return []
#Adding the difrent things to the board
def add_to_board(board, x, y, unit):
    board[y].append([(x, unit)])
def add_wall(board, x, y):
    add_to_board(board, x, y, "#")
def add_box(board, x, y):
    add_to_board(board, x, y, "o")
def add_storage_area(board, x, y):
    add_to_board(board, x, y, ".")
def add_box_in_storage(board, x, y):
    add_to_board(board, x, y, "*")
def add_player_in_storage(board, x, y):
    add_to_board(board, x, y, "+")
def creat_player(board, x, y):
    add_to_board(board, x, y, "@")


#
#Display board
#A board should be drawn on a upside down XY cordinate system
#ADT view
'''
def get_max_x(boamax(board[][])
rd):
def get_symbol(x, y)
'''
#player view
def display_board(board):
    max_x = get_max_x(board) 
    max_y = get_max_y(board) 
    for x in range(1, max_x + 1):
        for y in range(1, max_y + 1):
            symbol = get_symbol(x, y) 
            print(symbol, end="")
        print()
#
#cheack a cordinate on the board
#
#move player
#Make your move (a)left, (d)right, (w)up, (s)down: l
#
#cheack collision with player
#
#move box
#
#read file 
#
#convert file.txt to board
#
#chose a level
#
#play game 
#
#victory massage 
#

board = create_board()
add_wall(board, 1, 0)
add_wall(board, 0, 1)
add_wall(board, 2, 1)
add_wall(board, 1, 2)
creat_player(board, 1, 1)
print(board)