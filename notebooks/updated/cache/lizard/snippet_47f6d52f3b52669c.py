def crop(self, min, max):
    new = [c for c in self.coordinates if all(c >= min) and all(c < max)]
    return one(new)