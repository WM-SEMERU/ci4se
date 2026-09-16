def _get_image(self):
    if self.image is None:
        image_path = '%s/%s' % (current_app.static_folder, os.path.normpath
            (self.image_path))
        try:
            self.image = Image.open(image_path)
            self._reduce_opacity()
        except Exception as err:
            raise ValueError('Unsupported watermark format: %s' % str(err))
    return self.image