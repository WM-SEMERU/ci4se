def isLearned(self, mode=None):
    if 'l' in self.mode:
        return 1
    if 'h' in self.mode:
        return 0
    if 'a' in self.mode:
        if mode is None:
            mode = 'ql'
        if 'h' in mode and 'l' not in mode:
            return 0
    return 1