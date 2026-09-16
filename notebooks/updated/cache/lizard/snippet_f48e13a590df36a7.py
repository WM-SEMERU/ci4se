def get_deep_features(audio_data, verbose=True):
    from ._audio_feature_extractor import _get_feature_extractor
    if not _is_audio_data_sarray(audio_data):
        raise TypeError('Input must be audio data')
    feature_extractor_name = 'VGGish'
    feature_extractor = _get_feature_extractor(feature_extractor_name)
    return feature_extractor.get_deep_features(audio_data, verbose=verbose)