def setCenter(self, loc):
    offset = self.getCenter().getOffset(loc)
    return self.setLocation(self.getTopLeft().offset(offset))