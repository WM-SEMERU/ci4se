def _jsmin(self):
    self.theA = '\n'
    self._action(3)
    while self.theA != '\x00':
        if self.theA == ' ':
            if isAlphanum(self.theB):
                self._action(1)
            else:
                self._action(2)
        elif self.theA == '\n':
            if self.theB in ['{', '[', '(', '+', '-']:
                self._action(1)
            elif self.theB == ' ':
                self._action(3)
            elif isAlphanum(self.theB):
                self._action(1)
            else:
                self._action(2)
        elif self.theB == ' ':
            if isAlphanum(self.theA):
                self._action(1)
            else:
                self._action(3)
        elif self.theB == '\n':
            if self.theA in ['}', ']', ')', '+', '-', '"', "'"]:
                self._action(1)
            elif isAlphanum(self.theA):
                self._action(1)
            else:
                self._action(3)
        else:
            self._action(1)