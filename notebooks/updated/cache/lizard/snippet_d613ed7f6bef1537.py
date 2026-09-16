def count_never_executed(self):
    lineno = self.firstlineno
    counter = 0
    for line in self.source:
        if self.sourcelines.get(lineno) == 0:
            if not self.blank_rx.match(line):
                counter += 1
        lineno += 1
    return counter