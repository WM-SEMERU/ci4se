def load_fits(self, filepath):
    image = AstroImage.AstroImage(logger=self.logger)
    image.load_file(filepath)
    self.set_image(image)