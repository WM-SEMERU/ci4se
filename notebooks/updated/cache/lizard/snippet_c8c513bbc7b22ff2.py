def readlines(self, sizehint=None):
    wrapped = self.wrapped
    try:
        readlines = wrapped.readlines
    except AttributeError:
        lines = []
        while 1:
            line = wrapped.readline()
            if line:
                lines.append(line)
            else:
                break
        return lines
    return readlines() if sizehint is None else readlines(sizehint)