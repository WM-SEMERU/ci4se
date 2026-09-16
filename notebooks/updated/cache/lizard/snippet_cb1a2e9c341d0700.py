def create(self, width=0, max_value=0, path=None, flags=0, seed=0):
    return _madoka.Sketch_create(self, width, max_value, path, flags, seed)