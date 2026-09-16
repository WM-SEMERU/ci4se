def encode_all_features(dataset, vocabulary):

    def my_fn(features):
        ret = {}
        for k, v in features.items():
            v = vocabulary.encode_tf(v)
            v = tf.concat([tf.to_int64(v), [1]], 0)
            ret[k] = v
        return ret
    return dataset.map(my_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)