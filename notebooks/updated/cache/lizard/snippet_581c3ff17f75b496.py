def query(self, dataset, label=None, k=5, radius=None, verbose=True):
    _tkutl._raise_error_if_not_sframe(dataset, 'dataset')
    _tkutl._raise_error_if_sframe_empty(dataset, 'dataset')
    ref_features = self.features
    sf_features = _tkutl._toolkits_select_columns(dataset, ref_features)
    if label is None:
        query_labels = _turicreate.SArray.from_sequence(len(dataset))
    else:
        if not label in dataset.column_names():
            raise ValueError(
                "Input 'label' must be a string matching the name of a " +
                "column in the reference SFrame 'dataset'.")
        if not dataset[label].dtype == str and not dataset[label].dtype == int:
            raise TypeError(
                'The label column must contain integers or strings.')
        if label in ref_features:
            raise ValueError('The label column cannot be one of the features.')
        query_labels = dataset[label]
    if k is not None:
        if not isinstance(k, int):
            raise ValueError("Input 'k' must be an integer.")
        if k <= 0:
            raise ValueError("Input 'k' must be larger than 0.")
    if radius is not None:
        if not isinstance(radius, (int, float)):
            raise ValueError("Input 'radius' must be an integer or float.")
        if radius < 0:
            raise ValueError("Input 'radius' must be non-negative.")
    if k is None:
        k = -1
    if radius is None:
        radius = -1.0
    opts = {'model': self.__proxy__, 'model_name': self.__name__,
        'features': sf_features, 'query_labels': query_labels, 'k': k,
        'radius': radius}
    with QuietProgress(verbose):
        result = _turicreate.extensions._nearest_neighbors.query(opts)
    return result['neighbors']