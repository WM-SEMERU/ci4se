def _optionalPrompt(self, mode):
    if self.mode == 'h' or self.mode == 'a' and mode == 'h':
        if not self.isLegal():
            self.getWithPrompt()
    elif self.mode == 'u':
        if not self.isLegal():
            raise ValueError(
                "Attempt to access undefined local variable `%s'" % self.name)
    elif self.isCmdline() == 0:
        self.getWithPrompt()