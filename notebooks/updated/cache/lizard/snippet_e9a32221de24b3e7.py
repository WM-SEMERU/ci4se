def write_line(self, line=None, *args, **kwargs):
    if line is None:
        self.write('\n')
    else:
        if args or kwargs:
            line = line.format(*args, **kwargs)
        with self.__lock:
            self.write(line)
            try:
                if line[-1] != '\n':
                    self.write('\n')
            except IndexError:
                self.write('\n')
    self.flush()