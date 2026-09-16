def left(self, expand=None):
    if expand == None:
        x = 0
        y = self.y
        w = self.x
        h = self.h
    else:
        x = self.x - expand
        y = self.y
        w = expand
        h = self.h
    return Region(x, y, w, h).clipRegionToScreen()