def load_hdu(self, hdu):
    image = AstroImage.AstroImage(logger=self.logger)
    image.load_hdu(hdu)
    self.set_image(image)