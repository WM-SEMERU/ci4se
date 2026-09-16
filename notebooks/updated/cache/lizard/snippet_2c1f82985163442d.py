def index(self, x, y):
    col, row = [math.floor(a) for a in ~self.affine * (x, y)]
    return row, col