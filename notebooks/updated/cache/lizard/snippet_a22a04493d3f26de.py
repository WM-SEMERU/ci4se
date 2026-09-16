def _closure(self, target):
    closure = set()

    def collect(current):
        closure.add(current)
        return True
    self._walk(target, collect)
    return closure