import os
from lab4adt import *
from getkey import getkey, keys

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

#cheack collision with box
def box_can_move(board, direction, x, y):
    if direction == "left": 
        new_x = x - 1
        symbol = get_symbol(board, new_x, y)
    if direction == "right":
        new_x = x + 1
        symbol = get_symbol(board, new_x, y)
    if direction == "up":
        new_y = y - 1
        symbol = get_symbol(board, x, new_y)
    if direction == "down":
        new_y = y + 1 
        symbol = get_symbol(board, x, new_y) 

    match symbol:
        case " ":
            return True
        case "o":
            return False
        case ".":
            return True
        case "*":          
            return False
        case "#":
            return False
#move box
                       
def move_box(board, direction, x, y):
    element_old = get_element(board, x, y)
    symbolold = get_symbol(board, x, y)
    if direction == "left": 
        new_x = x - 1
        new_y = y 
        element = get_element(board, new_x ,new_y)
    if direction == "right":
        new_x = x + 1
        new_y = y
        element = get_element(board, new_x ,new_y)
    if direction == "up":
        new_y = y - 1
        new_x = x
        element = get_element(board, new_x ,new_y)
    if direction == "down":
        new_y = y + 1
        new_x = x 
        element = get_element(board, new_x ,new_y)
        
    if symbolold == "*":
        add_storage_area(board, x, y)
    if element == None:
        add_box(board, new_x, new_y)
    elif get_symbol(board, new_x ,new_y) == ".":
        board.remove(element)
        add_box_in_storage(board, new_x, new_y) 
    else:
        add_box(board, new_x, new_y)
    board.remove(element_old)

# 

#cheack collision with player

def player_can_move(board, direction, x, y):
    symbol = get_symbol(board, x, y)
    match symbol:
        case " ":
            return True
        case "o":
            box_movable = box_can_move(board, direction, x, y)
            if box_movable == True:
                move_box(board, direction, x, y)
                return True
            else:
                return False
        case ".":
            return True
        case "*":
            box_movable = box_can_move(board, direction, x, y)
            if box_movable == True:
                move_box(board, direction, x, y)
                return True
            else:
                return False
        case "#":
            return False
#  
#Flyttar spelaren
def update_player_position(board, new_x, new_y):
    element = get_element(board, new_x ,new_y)
    player = get_player(board)
    if get_player_symbol(board) == "+":
        add_storage_area(board, get_player_x(board), get_player_y(board))
    board.remove(player)
    if element == None:
        create_player(board, new_x, new_y)
    elif get_symbol(board, new_x ,new_y) == ".":
        board.remove(element)
        add_player_in_storage(board, new_x, new_y) 
    else:
        create_player(board, new_x, new_y)

#user
#väljer åt vilket håll som spelaren ska flytta sig 
def player_move_left(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_x = current_x - 1
    player_movement = player_can_move(board, "left" , new_x, current_y)
    if player_movement == True:
        update_player_position(board, new_x, current_y) 

def player_move_right(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_x = current_x + 1
    player_movement = player_can_move(board, "right" , new_x, current_y)
    if player_movement == True:
        update_player_position(board, new_x, current_y) 

def player_move_up(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_y = current_y - 1
    player_movement = player_can_move(board, "up" , current_x, new_y)
    if player_movement == True:
        update_player_position(board, current_x, new_y) 

def player_move_down(board):
    current_x = get_player_x(board)
    current_y = get_player_y(board)
    new_y = current_y + 1
    player_movement = player_can_move(board, "down" , current_x, new_y)
    if player_movement == True:
        update_player_position(board, current_x, new_y) 

def victory(board):
    counter = 0
    vic = False
    for elemnet in board:
        if "o" in elemnet:
            counter += 1
    if counter == 0:
        vic = True
    return vic

#play the chosen level
def play_level(board):
    board_copy = board.copy()
    while True: 
        os.system('clear')
        display_board(board)
        if victory(board):
            print("You are victorius")
            break 
        print("w(up), s(down), a(left), d(right), m(main menu), r(reload), b(quit)")
        key = getkey()
        match key:
            case "b":
                break
            case "a":
                player_move_left(board)
            case "d":
                player_move_right(board)
            case "w":
                player_move_up(board)
            case "s":
                player_move_down(board)
            case "m":
                main()
            case "r":
                play_level(board_copy)

                
#
#read file 
def make_levels(levels):
    levels.append([])
    #Har impoterat levels från fil till Levels varialbel
    #read file
    #kommer behöva ändra raden under till aceptabel linux format senare
    with open("Levels.txt", "r", encoding="UTF-8") as f:
        level = 0
        counter = 0
        for line in f: 
            if line == "\n":
                level += 1
                counter = 0
                levels.append([])
            levels[level].insert(counter, line)
            counter += 1
        f.close()
    return levels
#
#convert raw file imports to boards
def convert_raw_levels_to_boards(levels):
    temp = []
    for level in levels:
        board = create_board()
        y = 0
        for line in level:  
               x = 0  
               for character in line:    
                    match character:
                        case "o":
                            add_box(board, x, y)
                        case ".":
                            add_storage_area(board, x, y)
                        case "@":
                            create_player(board, x, y)
                        case "#":
                            add_wall(board, x, y)
                    x += 1
               y += 1 
        temp.append(board)       
    return temp

#main_game
def main():
    levels = []
    levels = make_levels(levels)
    levels = convert_raw_levels_to_boards(levels)
    print("Available levels")
    for i in range(len(levels)):
        print(f"Level {i + 1}")
    print("Press 0 to quit")
    chosen_level = int(input("Chose a level: "))
    if chosen_level != 0 :
        play_level(levels[chosen_level - 1])
main()