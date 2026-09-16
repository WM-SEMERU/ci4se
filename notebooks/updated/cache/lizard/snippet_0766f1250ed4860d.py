def post_process(self):
    self.image.putdata(self.pixels)
    self.image = self.image.transpose(Image.ROTATE_90)