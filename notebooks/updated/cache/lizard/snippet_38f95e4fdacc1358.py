def image2working(self, i):
    return self.colorspace.convert(self.image_space, self.working_space, i)