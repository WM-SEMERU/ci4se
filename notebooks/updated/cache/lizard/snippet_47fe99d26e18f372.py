def grid(self, z_x_y):
    z, x, y = z_x_y
    content = self.reader.grid(z, x, y, self.grid_fields, self.grid_layer)
    return content