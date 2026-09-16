def save_plain_image_as_file(self, filepath, format='png', quality=90):
    pixbuf = self.get_plain_image_as_pixbuf()
    options = {}
    if format == 'jpeg':
        options['quality'] = str(quality)
    pixbuf.save(filepath, format, options)