import lab4_board # We need to insert and move the player on the board

# TODO: This implementation is very naive
    # It assumes it can move anywhere and relies on other modules to raise exceptions
    # This is insufficient as a proper solution

def create_player(position_x: int, position_y: int):
    lab4_board.remove_object(lab4_board.get_item(-1, -1, "player"))
    lab4_board.add_item(position_x, position_y, "player")

def move(new_position_x: int, new_position_y: int):
    return

def can_move():
    return
