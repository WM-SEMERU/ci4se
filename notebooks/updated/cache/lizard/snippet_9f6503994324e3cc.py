def decode_single_feature_from_dict(feature_k, feature, tfexample_dict):
    if not feature.serialized_keys:
        data_to_decode = tfexample_dict[feature_k]
    else:
        data_to_decode = {k: tfexample_dict[posixpath.join(feature_k, k)] for
            k in feature.serialized_keys}
    return feature.decode_example(data_to_decode)