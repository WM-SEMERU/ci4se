def beginning_of_line(self):
    r
    if self.pos > len(self.string):
        return None
    elif self.pos == 0:
        return True
    return self.string[self.pos - 1] == '\n'