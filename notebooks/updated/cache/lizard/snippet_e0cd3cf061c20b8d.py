def output(self, value, normal=False, color=None, error=False, arrow=False,
    indent=None):
    if error and value and (normal or self.verbose):
        return self._print(value, color='red', indent=indent)
    if self.verbose or normal:
        return self._print(value, color, arrow, indent)
    return