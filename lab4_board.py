import warnings

# Items are saved in list as tuples:
    # Example: player = (pos_x: int, pos_y: int, item: str)

gameboard: list[tuple[int, int, str]] = []

# Returns true if the item exists in gameboard
    # False otherwise
def assert_item(item: tuple[int, int, str]) -> bool:
    if item in gameboard:
        return True
    else:
        return False

# Get an object from a given xy position
    # Returns tuple with negative positions and empty string if nothing is found
    # If type is defined it will only return filtered by that type
        # Useful for checking if a given type is on said position when types overlap
    # If either position is negative and type is specified it will look for the first occurence of said type
def get_item(position_x: int, position_y: int, type: str = "") -> tuple[int, int, str]:
    # If either position is negative: look for first occuring type
    if position_x < 0 or position_y < 0 and type != "":
        for item in gameboard:
            if item[2] == type:
                return item
    for item in gameboard:
        if type == "" and item[0] == position_x and item[1] == position_y:
            # Return item if type is empty string and positions match
            return item
        if item[2] == type and item[0] == position_x and item[1] == position_y:
            # Return item if type matches item type and positions match
            return item
    return (-1, -1, "")

# Adds a new item to the gameboard
    # Will raise exception if a duplicate already exists on the same tile
    # Will raise exception if type is not a string
    # Returns nothing
def add_item(position_x: int, position_y: int, type: str):
    if not isinstance(type, str): # Make sure type is a string
        raise TypeError("Tried adding an item to gameboard that was not a valid string!\nType was {type}\n")
    
    if not get_item(position_x, position_y, type) == "": # There can't be duplicates on the same tile
        raise AssertionError("Tried to add an item that already exists at the specified position!\nPosition was {position_x}, {position_y}: {type}")
    
    gameboard.append((position_x, position_y, type))

# Remove an item from the gameboard
    # Will raise exception if the item doesn't exist or type is invalid string
    # Returns nothing
def remove_item(position_x: int, position_y: int, type: str):
    if not isinstance(type, str): # Make sure type is a string
        raise TypeError("Tried to remove an item from the gameboard that was not a valid string!\nType was {type}\n")
    
    if get_item(position_x, position_y, type) == "": # Assert that there is something to be removed
        raise AssertionError("Tried to remove an item that doesn't exists at the specified position!\nPosition was {position_x}, {position_y}: {type}")

    # Should never raise an exception if previous asserts function properly
    gameboard.remove((position_x, position_y, type))

# Remove an item from gameboard by object
    # Raises exception if object doesn't exist
def remove_object(item: tuple[int, int, str]):
    if not get_object(item):
        raise AssertionError("Tried to remove an item that doesn't exists at the specified position!\nPosition was {position_x}, {position_y}: {type}")
    gameboard.remove(item)

# Load a level from file
def load_level():
    # TODO: ADD!
    return