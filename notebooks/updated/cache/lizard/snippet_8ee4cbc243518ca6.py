def get_default_sticker_id(self):
    size = self.request.get('size', '')
    if size == 'small':
        return self.sample_type.getDefaultSmallSticker()
    return self.sample_type.getDefaultLargeSticker()