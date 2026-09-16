def _write_line(self, line=None):
    if line is None:
        self._write('\n')
        if self.__indent_level > 1:
            self.__indent_level -= 1
    elif line == '':
        self._write('\n')
    else:
        line = ' ' * 4 * self.__indent_level + line
        if line[-1:] == ':':
            self.__indent_level += 1
        self._write(line + '\n')