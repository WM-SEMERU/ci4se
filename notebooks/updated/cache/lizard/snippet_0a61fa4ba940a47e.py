def op(name, images, max_outputs=3, display_name=None, description=None,
    collections=None):
    import tensorflow.compat.v1 as tf
    if display_name is None:
        display_name = name
    summary_metadata = metadata.create_summary_metadata(display_name=
        display_name, description=description)
    with tf.name_scope(name), tf.control_dependencies([tf.assert_rank(
        images, 4), tf.assert_type(images, tf.uint8), tf.
        assert_non_negative(max_outputs)]):
        limited_images = images[:max_outputs]
        encoded_images = tf.map_fn(tf.image.encode_png, limited_images,
            dtype=tf.string, name='encode_each_image')
        image_shape = tf.shape(input=images)
        dimensions = tf.stack([tf.as_string(image_shape[2], name='width'),
            tf.as_string(image_shape[1], name='height')], name='dimensions')
        tensor = tf.concat([dimensions, encoded_images], axis=0)
        return tf.summary.tensor_summary(name='image_summary', tensor=
            tensor, collections=collections, summary_metadata=summary_metadata)