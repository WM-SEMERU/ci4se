def resize_image(image_str_tensor):
    image = decode_and_resize(image_str_tensor)
    image = tf.image.encode_jpeg(image, quality=100)
    return image