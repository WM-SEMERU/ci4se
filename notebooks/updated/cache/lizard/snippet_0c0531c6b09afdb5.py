def validate(self, path):
    if os.path.basename(path).startswith('.'):
        return False
    if not self.check_level(path):
        return False
    if self.filters:
        if not self._level_filters(path):
            return False
    if self.to_exclude:
        if any(str(ex).lower() in path.lower() for ex in self.to_exclude):
            return False
    if self.to_include:
        if not any(str(inc).lower() in path.lower() for inc in self.to_include
            ):
            return False
    return True