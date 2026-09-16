def _decode_input_tensor_to_features_dict(feature_map, hparams):
    inputs = tf.convert_to_tensor(feature_map['inputs'])
    input_is_image = False
    x = inputs
    p_hparams = hparams.problem_hparams
    x = tf.expand_dims(x, axis=[2])
    x = tf.to_int32(x)
    input_space_id = tf.constant(p_hparams.input_space_id)
    target_space_id = tf.constant(p_hparams.target_space_id)
    features = {}
    features['input_space_id'] = input_space_id
    features['target_space_id'] = target_space_id
    features['decode_length'
        ] = IMAGE_DECODE_LENGTH if input_is_image else tf.shape(x)[1] + 50
    features['inputs'] = x
    return features