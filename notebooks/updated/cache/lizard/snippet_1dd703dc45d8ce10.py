def set_image(self, image=None):
    if image is None or type(image) is not int:
        raise KPError('Need a new image number')
    else:
        self.image = image
        self.last_mod = datetime.now().replace(microsecond=0)
        return True