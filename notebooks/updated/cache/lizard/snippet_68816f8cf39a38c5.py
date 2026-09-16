def load_conll(f, features, n_features=2 ** 16, split=False):
    fh = FeatureHasher(n_features=n_features, input_type='string')
    labels = []
    lengths = []
    with _open(f) as f:
        raw_X = _conll_sequences(f, features, labels, lengths, split)
        X = fh.transform(raw_X)
    return X, np.asarray(labels), np.asarray(lengths, dtype=np.int32)