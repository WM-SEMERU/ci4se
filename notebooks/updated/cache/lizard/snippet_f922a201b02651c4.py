def _select_features(example, feature_list=None):
    feature_list = feature_list or ['inputs', 'targets']
    return {f: example[f] for f in feature_list}