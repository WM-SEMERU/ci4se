def check(labels):
    if not isinstance(labels, list):
        raise IOError('labels are not in a list')
    if not len(labels):
        raise IOError('the labels list is empty')
    if not all([isinstance(l, np.ndarray) for l in labels]):
        raise IOError('all labels must be numpy arrays')
    ndim = labels[0].ndim
    if ndim not in [1, 2]:
        raise IOError('labels dimension must be 1 or 2')
    if not all([(l.ndim == ndim) for l in labels]):
        raise IOError('all labels dimensions must be equal')
    if ndim == 2:
        shape1 = labels[0].shape[1]
        if not all([(l.shape[1] == shape1) for l in labels]):
            raise IOError('all labels must have same shape on 2nd dim')
    for label in labels:
        index = np.argsort(label) if label.ndim == 1 else np.lexsort(label.T)
        assert len(index) == label.shape[0]
        if not all(n == index[n] for n in range(label.shape[0] - 1)):
            raise IOError('labels are not sorted in increasing order')