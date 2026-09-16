def set_image(self, image):
    image = self.manager.get_abs_image_path(image)
    yield from self._hypervisor.send('vm set_ios "{name}" "{image}"'.format
        (name=self._name, image=image))
    log.info('Router "{name}" [{id}]: has a new IOS image set: "{image}"'.
        format(name=self._name, id=self._id, image=image))
    self._image = image