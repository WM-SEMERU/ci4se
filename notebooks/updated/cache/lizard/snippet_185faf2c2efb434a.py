def index(self, item):
    for i, x in enumerate(self.iter()):
        if x == item:
            return i
    return None