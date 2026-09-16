def is_excluded(self, path, exclude=None):
    for pattern in (exclude or self.exclude_pattern):
        if path.match(pattern):
            return True
    else:
        return False