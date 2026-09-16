def image(name, data, step=None, max_outputs=3, description=None):
    summary_metadata = metadata.create_summary_metadata(display_name=None,
        description=description)
    summary_scope = getattr(tf.summary.experimental, 'summary_scope', None
        ) or tf.summary.summary_scope
    with summary_scope(name, 'image_summary', values=[data, max_outputs, step]
        ) as (tag, _):
        tf.debugging.assert_rank(data, 4)
        tf.debugging.assert_non_negative(max_outputs)
        images = tf.image.convert_image_dtype(data, tf.uint8, saturate=True)
        limited_images = images[:max_outputs]
        encoded_images = tf.map_fn(tf.image.encode_png, limited_images,
            dtype=tf.string, name='encode_each_image')
        encoded_images = tf.cond(tf.shape(input=encoded_images)[0] > 0, lambda
            : encoded_images, lambda : tf.constant([], tf.string))
        image_shape = tf.shape(input=images)
        dimensions = tf.stack([tf.as_string(image_shape[2], name='width'),
            tf.as_string(image_shape[1], name='height')], name='dimensions')
        tensor = tf.concat([dimensions, encoded_images], axis=0)
        return tf.summary.write(tag=tag, tensor=tensor, step=step, metadata
            =summary_metadata)