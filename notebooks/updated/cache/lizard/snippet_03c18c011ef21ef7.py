def is_valid_tile(self, x, y):
    x = int(x)
    y = int(y)
    if x < 0:
        return False
    if y < 0:
        return False
    if x > self.size_in_tiles.X:
        return False
    if y > self.size_in_tiles.Y:
        return False
    return True