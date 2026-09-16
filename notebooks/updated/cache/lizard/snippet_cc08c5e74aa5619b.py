def add_image_history(self, data):
    self._ef['0th'][piexif.ImageIFD.ImageHistory] = json.dumps(data)