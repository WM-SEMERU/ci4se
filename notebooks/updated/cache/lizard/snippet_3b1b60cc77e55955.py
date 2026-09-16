def _center_crop(image, size):
    image_height = tf.shape(image)[0]
    image_width = tf.shape(image)[1]
    offset_height = (image_height - size + 1) / 2
    offset_width = (image_width - size + 1) / 2
    image = _crop(image, offset_height, offset_width, size, size)
    return image