def affine(self, pixelbuffer=0):
    return Affine(self.pixel_x_size, 0, self.bounds(pixelbuffer).left, 0, -
        self.pixel_y_size, self.bounds(pixelbuffer).top)