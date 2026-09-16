def _contains(self, item):
    if self is item:
        return True
    for m in self.modules:
        if item in m:
            return True
    for p in self.packages:
        if item in p:
            return True
    return False