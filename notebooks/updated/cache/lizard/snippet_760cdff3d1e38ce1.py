def filter_bad_names(self, images):
    good_images = []
    for image in images:
        if self.is_valid_filename(image):
            good_images.append(image)
    return good_images if len(good_images) > 0 else None