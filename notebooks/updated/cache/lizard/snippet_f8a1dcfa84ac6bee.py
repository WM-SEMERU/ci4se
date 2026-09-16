def load(self, image=None):
    from spython.image import Image
    from spython.instance import Instance
    self.simage = Image(image)
    if image is not None:
        if image.startswith('instance://'):
            self.simage = Instance(image)
        bot.info(self.simage)