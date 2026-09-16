def add(self, *args):
    for fn in args:
        self.warn_if_function_not_registered(fn)
        self._stack.append(fn)