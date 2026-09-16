def convert_labels(Y, source, dest):
    if Y is None:
        return Y
    if isinstance(Y, np.ndarray):
        Y = Y.copy()
        assert isinstance(Y, int)
    elif isinstance(Y, torch.Tensor):
        Y = Y.clone()
        assert np.sum(Y.numpy() - Y.numpy().astype(int)) == 0.0
    else:
        raise ValueError('Unrecognized label data type.')
    negative_map = {'categorical': 2, 'plusminus': -1, 'onezero': 0}
    Y[Y == negative_map[source]] = negative_map[dest]
    return Y