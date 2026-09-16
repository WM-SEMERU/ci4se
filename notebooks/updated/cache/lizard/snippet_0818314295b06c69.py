def to_string(direction):
    if direction == UP:
        return UP
    elif direction == DOWN:
        return DOWN
    elif direction == LEFT:
        return LEFT
    elif direction == RIGHT:
        return RIGHT
    else:
        raise InvalidDirectionError(type_string)