import os
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



#player view
#display board must be outside adt 
def display_board(board):
    max_x = get_max_x(board) 
    max_y = get_max_y(board) 
    for y in range(max_y+1):
        for x in range(max_x+1):
            symbol = get_symbol(board, x, y) 
            print(symbol, end="")
        print("")
#
#cheack a cordinate on the board
#
#move player
#Make your move (a)left, (d)right, (w)up, (s)down: l
#ADT
def get_player(board):
    for element in board:
        if element[0] == "@":
            return element

def get_player_x(board):
    element = get_player(board)
    return element[1]

def get_player_y(board):
    element = get_player(board)
    return element[2]

"""def cheack_collision(board, x, y):
    collision = False
    symbol = get_symbol(board, x, y)
    if symbol != " ":
        collision = True
    return collision
   """
def cheack_collision_nonplayer(board, x, y):
    symbol = get_symbol(board, x, y)
    empty_position = False
    if symbol == " ":
        empty_position = True
        print(empty_position)
    return empty_position

def move_left(board, current_x, current_y):
    new_x = current_x - 1
    empty_position = cheack_collision_nonplayer(board, new_x, current_y)


def move_rigth(board, current_x, current_y):
    new_x = current_x + 1
    empty_position = cheack_collision_nonplayer(board, new_x, current_y)


def move_up(board, current_x, current_y):
    new_y = current_y - 1 
    empty_position = cheack_collision_nonplayer(board, current_x, new_y)


def move_down(board, current_x, current_y):
    new_y = current_y + 1
    empty_position = cheack_collision_nonplayer(board, current_x, new_y)

                           
def move_box(board, direction, x, y):
    if direction == "left": 
        move_left(board, x, y)
    if direction == "rigth":
        move_rigth(board, x, y)
    if direction == "up":
        move_up(board, x, y)
    if direction == "down":
        move_down(board, x, y)

def cheack_collision_player(board, direction, x, y):
    symbol = get_symbol(board, x, y)
    match symbol:
        case " ":
            pass
        case "o":
            move_box(board, direction, x, y)
            
        case ".":
            pass
        case "*":
            pass
        case "#":
            pass

def update_player_position(board, new_x, new_y):
    player = get_player(board)
    empty_position = cheack_collision_nonplayer(board, new_x, new_y)
    if empty_position == True:
        board.remove(player)
        create_player(board, new_x, new_y)
        player = get_player(board)
        print(player)

#user
def player_move_left(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_x = current_x - 1
    cheack_collision_player(board, "left" , new_x, current_y)
    update_player_position(board, new_x, current_y) 

def player_move_right(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_x = current_x + 1
    cheack_collision_player(board, "right" ,new_x,current_y)
    update_player_position(board, new_x, current_y)

def player_move_up(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_y = current_y - 1
    cheack_collision_player(board,"up" ,  current_x, new_y)
    update_player_position(board, current_x, new_y)

def player_move_down(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_y = current_y + 1
    cheack_collision_player(board, "down" , current_x, new_y)
    update_player_position(board, current_x, new_y)

   

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
def main_game(board):
    while True:
        os.system('clear')
        display_board(board)
        player_decision = input("Skriv en input ")
        match player_decision:
            case "b":
                print("Väl spelat")
                break
            case "a":
                player_move_left(board)
            case "d":
                player_move_right(board)
            case "w":
                player_move_up(board)
            case "s":
                player_move_down(board)

#
#victory massage 
#

board = create_board()
#ROW 0
for n in range(4, 9):
    add_wall(board,n,0)

#ROW 1
add_wall(board, 4, 1)
add_wall(board, 8, 1)

#ROW 2
add_wall(board, 4, 2)
add_wall(board, 8, 2)

#ROW 3
add_wall(board, 4, 3)
add_box(board, 5, 3)
add_wall(board, 8, 3)

#ROW 4
add_wall(board, 2, 4)
add_wall(board, 3, 4)
add_wall(board, 4, 4)
add_box(board, 7, 4)
add_wall(board, 8, 4)
add_wall(board, 9, 4)

#ROW 5
add_wall(board, 2, 5)
add_box(board, 5, 5)
add_box(board, 7, 5)
add_wall(board, 9, 5)

#ROW 6
add_wall(board, 0, 6)
add_wall(board, 1, 6)
add_wall(board, 2, 6)
add_wall(board, 4, 6)
add_wall(board, 6, 6)
add_wall(board, 7, 6)
add_wall(board, 9, 6)
add_wall(board, 13, 6)
add_wall(board, 14, 6)
add_wall(board, 15, 6)
add_wall(board, 16, 6)
add_wall(board, 17, 6)
add_wall(board, 18, 6)

#ROW 7
add_wall(board, 0, 7)
add_wall(board, 4, 7)
add_wall(board, 6, 7)
add_wall(board, 7, 7)
add_wall(board, 9, 7)
add_wall(board, 10, 7)
add_wall(board, 11, 7)
add_wall(board, 12, 7)
add_wall(board, 13, 7)
add_storage_area(board, 16, 7)
add_storage_area(board, 17, 7)
add_wall(board, 18, 7)

#ROW 8
add_wall(board, 0, 8)
add_box(board, 2, 8)
add_box(board, 5, 8)
add_storage_area(board, 16, 8)
add_storage_area(board, 17, 8)
add_wall(board,18, 8)

#ROW 9
add_wall(board, 0, 9)
add_wall(board, 1, 9)
add_wall(board, 2, 9)
add_wall(board, 3, 9)
add_wall(board, 4, 9)
add_wall(board, 6, 9)
add_wall(board, 7, 9)
add_wall(board, 8, 9)
add_wall(board, 10, 9)
create_player(board, 11, 9)
add_wall(board, 12, 9)
add_wall(board, 13, 9)
add_storage_area(board, 16, 9)
add_storage_area(board, 17, 9)
add_wall(board, 18, 9)

#ROW 10
add_wall(board, 4, 10)
add_wall(board, 10, 10)
add_wall(board, 11, 10)
add_wall(board, 12, 10)
add_wall(board, 13, 10)
add_wall(board, 14, 10)
add_wall(board, 15, 10)
add_wall(board, 16, 10)
add_wall(board, 17, 10)
add_wall(board, 18, 10)

#ROW 11
add_wall(board, 4, 11)
add_wall(board, 5, 11)
add_wall(board, 6, 11)
add_wall(board, 7, 11)
add_wall(board, 8, 11)
add_wall(board, 9, 11)
add_wall(board, 10, 11)
main_game(board)