def linenum(self, index):
    if len(self._lines) == 0 and self.refstring != '':
        self._lines = self.refstring.split('\n')
        self._chars = [(len(x) + 1) for x in self._lines]
        self._chars[-1] -= 1
        total = 0
        for i in range(len(self._chars)):
            total += self._chars[i]
            self._chars[i] = total
    if len(self._lines) > 0:
        result = -1
        i = 0
        while result == -1 and i < len(self._chars):
            if index <= self._chars[i]:
                result = [i, self._chars[i] - index]
            i += 1
        return result
    else:
        return [-1, -1]