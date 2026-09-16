def get_data(self, data_x, data_y):
    image = self.get_image()
    if image is not None:
        return image.get_data_xy(data_x, data_y)
    raise ImageViewNoDataError('No image found')