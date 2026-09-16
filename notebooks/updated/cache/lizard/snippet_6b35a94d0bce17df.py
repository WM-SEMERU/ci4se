def fix_e305(self, result):
    cr = '\n'
    offset = result['line'] - 2
    while True:
        if offset < 0:
            break
        line = self.source[offset].lstrip()
        if len(line) == 0:
            break
        if line[0] != '#':
            break
        offset -= 1
    offset += 1
    self.source[offset] = cr + self.source[offset]