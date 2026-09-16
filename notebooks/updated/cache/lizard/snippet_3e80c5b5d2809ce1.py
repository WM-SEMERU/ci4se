def skip(self, chars=spaceCharactersBytes):
    p = self.position
    while p < len(self):
        c = self[p:p + 1]
        if c not in chars:
            self._position = p
            return c
        p += 1
    self._position = p
    return None