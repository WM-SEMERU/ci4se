def baseoffset(self):
    try:
        return self.parent.baseoffset + self.offset
    except AttributeError:
        return self.offset