def op(scalars_layout, collections=None):
    import tensorflow.compat.v1 as tf
    assert isinstance(scalars_layout, layout_pb2.Layout)
    summary_metadata = metadata.create_summary_metadata()
    return tf.summary.tensor_summary(name=metadata.CONFIG_SUMMARY_TAG,
        tensor=tf.constant(scalars_layout.SerializeToString(), dtype=tf.
        string), collections=collections, summary_metadata=summary_metadata)