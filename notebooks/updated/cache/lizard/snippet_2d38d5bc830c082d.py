def fix_e301(self, result):
    cr = '\n'
    self.source[result['line'] - 1] = cr + self.source[result['line'] - 1]