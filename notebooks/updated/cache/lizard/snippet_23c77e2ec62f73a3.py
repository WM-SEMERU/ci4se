def cat_acc(y, z):
    weights = _cat_sample_weights(y)
    _acc = K.cast(K.equal(K.argmax(y, axis=-1), K.argmax(z, axis=-1)), K.
        floatx())
    _acc = K.sum(_acc * weights) / K.sum(weights)
    return _acc