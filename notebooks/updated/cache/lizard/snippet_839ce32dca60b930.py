def set_size(self, position, size, padding):
    self.height = size
    self.position = position
    x = position[0]
    for key in self.keys:
        key.set_size(size)
        key.position = x, position[1]
        x += padding + key.size[0]