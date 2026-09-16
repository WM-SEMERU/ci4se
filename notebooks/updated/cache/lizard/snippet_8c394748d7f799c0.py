def get(feature, obj, **kwargs):
    feature = NEURITEFEATURES[feature
        ] if feature in NEURITEFEATURES else NEURONFEATURES[feature]
    return _np.array(list(feature(obj, **kwargs)))