def save_plain_image_as_file(self, filepath, format='png', quality=90):
    qimg = self.get_plain_image_as_widget()
    qimg.save(filepath, format=format, quality=quality)