def write(self, *data):
    for l in data:
        for i in str(l):
            if i == '\n':
                self.current_line_number += 1
                pass
            pass
        pass
    return super(LineMapWalker, self).write(*data)