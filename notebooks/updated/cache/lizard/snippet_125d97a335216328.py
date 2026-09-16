def setdefaultlist(self, key, defaultlist=[None]):
    if key in self:
        return self.getlist(key)
    self.addlist(key, defaultlist)
    return defaultlist