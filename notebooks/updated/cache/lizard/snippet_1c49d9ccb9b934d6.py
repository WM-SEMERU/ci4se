def end(self, *args):
    if self._is_verbose:
        return self
    if not args:
        self._indent -= 1
        return self
    self.writeln('end', *args)
    self._indent -= 1
    return self