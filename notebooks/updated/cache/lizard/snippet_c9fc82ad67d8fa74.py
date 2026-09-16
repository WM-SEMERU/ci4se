def build_tensor_serving_input_receiver_fn(shape, dtype=tf.float32,
    batch_size=1):

    def serving_input_receiver_fn():
        features = tf.placeholder(dtype=dtype, shape=[batch_size] + shape,
            name='input_tensor')
        return tf.estimator.export.TensorServingInputReceiver(features=
            features, receiver_tensors=features)
    return serving_input_receiver_fn