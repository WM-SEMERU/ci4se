def _vowelinstem(self, stem):
    for i in range(len(stem)):
        if not self._cons(stem, i):
            return True
    return False