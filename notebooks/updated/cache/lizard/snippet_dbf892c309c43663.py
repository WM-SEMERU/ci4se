def is_dynamic(self):
    if not self._static:
        for token, value in self.tokens():
            if token != 'TXT':
                return True
    self._static = True
    return False