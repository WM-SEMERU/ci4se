def create_feature_map(features, feature_indices, output_dir):
    feature_map = []
    for name, info in feature_indices:
        transform_name = features[name]['transform']
        source_column = features[name]['source_column']
        if transform_name in [IDENTITY_TRANSFORM, SCALE_TRANSFORM]:
            feature_map.append((info['index_start'], name))
        elif transform_name in [ONE_HOT_TRANSFORM, MULTI_HOT_TRANSFORM]:
            vocab, _ = read_vocab_file(os.path.join(output_dir, 
                VOCAB_ANALYSIS_FILE % source_column))
            for i, word in enumerate(vocab):
                if transform_name == ONE_HOT_TRANSFORM:
                    feature_map.append((info['index_start'] + i, '%s=%s' %
                        (source_column, word)))
                elif transform_name == MULTI_HOT_TRANSFORM:
                    feature_map.append((info['index_start'] + i, 
                        '%s has "%s"' % (source_column, word)))
        elif transform_name == IMAGE_TRANSFORM:
            for i in range(info['size']):
                feature_map.append((info['index_start'] + i, 
                    '%s image feature %d' % (source_column, i)))
    return feature_map