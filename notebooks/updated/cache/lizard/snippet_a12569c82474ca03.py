def validlines(self):
    return [ln for ln in self.lines() if not ln.isBroken() and not ln.ignoreMe]