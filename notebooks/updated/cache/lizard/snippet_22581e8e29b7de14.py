def _assign_ascii_character(self, y_prev, y, y_next):
    char = '?'
    if y_next > y and y_prev > y:
        char = '-'
    elif y_next < y and y_prev < y:
        char = '-'
    elif y_prev < y and y == y_next:
        char = '-'
    elif y_prev == y and y_next < y:
        char = '-'
    elif y_next > y:
        char = '/'
    elif y_next < y:
        char = '\\'
    elif y_prev < y:
        char = '/'
    elif y_prev > y:
        char = '\\'
    elif y_next == y:
        char = '-'
    elif y == y_prev:
        char = '-'
    return char