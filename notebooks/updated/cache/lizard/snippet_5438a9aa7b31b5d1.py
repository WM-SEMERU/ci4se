def precmd(self, line):
    line = self.prefix + line
    self._history += [line.strip()]
    return line