def contents(self):
    if not self._contents:
        if self._path:
            f = open(self._path, 'rb')
            self._contents = f.read()
            f.close()
        elif self._pil_image:
            f = StringIO()
            self._pil_image.save(f, self.format)
            self._contents = f.getvalue()
    return self._contents