def _random_crop(image, size):
    bbox = tf.constant([0.0, 0.0, 1.0, 1.0], dtype=tf.float32, shape=[1, 1, 4])
    random_image, bbox = distorted_bounding_box_crop(image, bbox,
        min_object_covered=0.1, aspect_ratio_range=(3.0 / 4, 4.0 / 3.0),
        area_range=(0.08, 1.0), max_attempts=1, scope=None)
    bad = _at_least_x_are_true(tf.shape(image), tf.shape(random_image), 3)
    image = tf.cond(bad, lambda : _center_crop(_do_scale(image, size), size
        ), lambda : tf.image.resize_bicubic([random_image], [size, size])[0])
    return image