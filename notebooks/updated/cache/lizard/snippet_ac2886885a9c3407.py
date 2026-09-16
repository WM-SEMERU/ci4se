def merge(self, other):
    for key in other.keys():
        if key not in self:
            self[key] = other[key]