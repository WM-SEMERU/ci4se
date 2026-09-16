def _openResources(self):
    with Image.open(self._fileName) as image:
        self._array = np.asarray(image)
        self._bands = image.getbands()
        self._attributes = dict(image.info)
        self._attributes['Format'] = image.format
        self._attributes['Mode'] = image.mode
        self._attributes['Size'] = image.size
        self._attributes['Width'] = image.width
        self._attributes['Height'] = image.height