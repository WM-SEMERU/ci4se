def generate(self):
    x, y, z = self.point1
    return x + self.size_x * random(), y + self.size_y * random(
        ), z + self.size_z * random()