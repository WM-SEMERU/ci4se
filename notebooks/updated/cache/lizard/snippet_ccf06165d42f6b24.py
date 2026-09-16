def previous(self, type=None):
    i = self.index - 1
    s = self.sentence
    while i > 0:
        if type in (s[i].type, None):
            return s[i]
        i -= 1