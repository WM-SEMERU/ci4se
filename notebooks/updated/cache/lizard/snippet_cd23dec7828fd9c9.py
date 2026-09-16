def op(name, data, display_name=None, description=None, collections=None):
    import tensorflow.compat.v1 as tf
    if display_name is None:
        display_name = name
    summary_metadata = metadata.create_summary_metadata(display_name=
        display_name, description=description)
    with tf.name_scope(name):
        with tf.control_dependencies([tf.assert_type(data, tf.string)]):
            return tf.summary.tensor_summary(name='text_summary', tensor=
                data, collections=collections, summary_metadata=
                summary_metadata)