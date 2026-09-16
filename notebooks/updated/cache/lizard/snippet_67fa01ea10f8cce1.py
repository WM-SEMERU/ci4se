def set(self, x, y):
    x = normalize(x)
    y = normalize(y)
    col, row = get_pos(x, y)
    if type(self.chars[row][col]) != int:
        return
    self.chars[row][col] |= pixel_map[y % 4][x % 2]