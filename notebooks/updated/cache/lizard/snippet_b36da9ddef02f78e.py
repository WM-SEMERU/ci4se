def update(self, *args, **kwargs):
    data = self._clean_data(*args, **kwargs)
    if 'images' in data:
        images = data['images']
        for img in images:
            self._update_image(img)
    else:
        self._update_data(data=data)