def save_intermediate_img(self, img, name):
    if self.intermediate_results:
        img.writeto(name, overwrite=True)