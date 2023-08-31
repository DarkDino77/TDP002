# Create the beginning board
# The board is a list of items where it stores secondary list of tuples
# where the secondary list position in the first list is the y cordinate
# And the tuple has the x  cordinate and wich peice it is information 
'''
# Internal representation:
# [
#  y = 0 [(1, "#"), (2, "@"), (3, "#")],
#  y = 1 [(1, "#"), (3, "#")]
# ]

'''
def create_board():
    return []
#Adding the difrent things to the board
def add_to_board(board, x, y, unit):
    if y > len(board) - 1:
        board.append([])
    if x > len(board[y]) - 1:
        board[y].append((x, unit))
    else: 
        board[y].insert(x, (x, unit))

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
    for lines in board:
        if max_x < len(lines) :
            max_x = len(lines) 
    return max_x

def get_max_y(board):
    return len(board)

def get_symbol(board, x, y):
    
    symbol = ""
    if board[y] not in board:
       # print("y")
        symbol = " "
    elif board[y][x][0] is not x :
        #print("x")
        symbol = " "
    else:
        symbol = board[y][x][1]
        
    '''
    symbol = " "
    print(len(board[y])-1, end=" ")
    print(x, end = "")
    if len(board[y])-1 < x:
        symbol = " "
    elif board[y][x][0] == x  :
  
        symbol = board[y][x][1]

    return symbol
     '''



#player view
#display board must be outside adt 
def display_board(board):
    max_x = get_max_x(board) 
    max_y = get_max_y(board) 
    for x in range(max_x):
        for y in range(max_y):
            symbol = get_symbol(board, x, y) 
            print(symbol, end="")
        print("")
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
display_board(board)
