#create the begining board
# The board is a list of items where it stores secondary list of tuples
# where the secondary list position in the first list is the y cordinate
# And the tuple has the x  cordinate and wich peice it is information 
'''
# Intern representation:
# [
#  y = 0 [(1, "#"), (2, "@"), (3, "#")],
#  y = 1 [(1, "#"), (3, "#")]
# ]

'''
def create_board():
    return []
#Adding the difrent things to the board
def add_to_board(board, x, y, unit):
    board.append((unit, x, y))

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

def get_max_x(board):
    max_x = 0
    for elements in board:
        if max_x < elements[1] :
            max_x = elements[1]

    return max_x

def get_max_y(board):
    max_y = 0
    for elements in board:
        if max_y < elements[2] :
            max_y = elements[2] 
    return max_y

def get_symbol(board, x, y):
    symbol = " "
    for element in board:
        if element[1] == x and element[2] == y:
            symbol = element[0]
        
    return symbol



#player view
#display board must be outside adt 
def display_board(board):
    max_x = get_max_x(board) 
    max_y = get_max_y(board) 
    for y in range(max_y+1):
        for x in range(max_x+1):
            symbol = get_symbol(board, x, y) 
            print(symbol, end="")
#
#cheack a cordinate on the board
#
#move player
#Make your move (a)left, (d)right, (w)up, (s)down: l
#ADT
def get_player_x(board):
    for element in board:
        if element[0] == "@":
            return element[1]
def get_player_y(board):
    for element in board:
        if element[0] == "@":
            return element[2]
#user
def player_move_left(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)

#def player_move_right(board):
#def player_move_up(board):    
#def player_move_down(board):    

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
add_wall(board, 0, 0)
add_wall(board, 1, 0)
add_wall(board, 2, 0)
add_wall(board, 3, 0)
add_wall(board, 4, 0)
add_wall(board, 5, 0)

add_wall(board, 0, 1)
add_wall(board, 0, 2)
add_wall(board, 1, 2)
add_wall(board, 2, 2)
add_wall(board, 3, 2)
add_wall(board, 4, 2)
add_wall(board, 5, 2)
add_wall(board, 5, 1)

add_box(board, 2,1)
add_storage_area(board, 4,1)
creat_player(board, 1, 1)
display_board(board)
