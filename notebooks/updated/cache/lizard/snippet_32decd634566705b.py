def visualize_tensors(name, imgs, scale_func=lambda x: (x + 1.0) * 128.0,
    max_outputs=1):
    xy = scale_func(tf.concat(imgs, axis=2))
    xy = tf.cast(tf.clip_by_value(xy, 0, 255), tf.uint8, name='viz')
    tf.summary.image(name, xy, max_outputs=30)