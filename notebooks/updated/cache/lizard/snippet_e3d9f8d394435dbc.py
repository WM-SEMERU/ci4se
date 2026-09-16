def put_standard_block(self, y, x, val):
    for j in range(0, self.cell_height):
        for i in range(0, self.cell_width):
            self.img.put(val, (x * self.cell_width + i, y * self.
                cell_height + j))