def right(self, expand=None):
    if expand == None:
        x = self.x + self.w
        y = self.y
        w = self.getScreen().getBounds()[2] - x
        h = self.h
    else:
        x = self.x + self.w
        y = self.y
        w = expand
        h = self.h
    return Region(x, y, w, h).clipRegionToScreen()