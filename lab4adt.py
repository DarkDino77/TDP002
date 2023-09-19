
#create the begining board
# The board is a list of items where it stores secondary list of tuples
# where the secondary list position in the first list is the y cordinate
# And the tuple has the x  cordinate and wich peice it is information 


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
def create_player(board, x, y):
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

def get_element(board, x, y):
    for element in board:
        if element[1] == x and element[2] == y:
            return element

def get_symbol(board, x, y):
    symbol = " "
    element = get_element(board, x, y)
    if element != None:
        symbol = element[0]      
    return symbol

#
#move player
#Make your move (a)left, (d)right, (w)up, (s)down: l
#ADT
def get_player(board):
    for element in board:
        if element[0] == "@" or element[0] == "+":
            return element

def get_player_x(board):
    element = get_player(board)
    return element[1]

def get_player_y(board):
    element = get_player(board)
    return element[2]

def get_player_symbol(board):
    player = get_player(board)
    return player[0]