def _infer_interval_breaks(coord, axis=0, check_monotonic=False):
    coord = np.asarray(coord)
    if check_monotonic and not _is_monotonic(coord, axis=axis):
        raise ValueError(
            'The input coordinate is not sorted in increasing order along axis %d. This can lead to unexpected results. Consider calling the `sortby` method on the input DataArray. To plot data with categorical axes, consider using the `heatmap` function from the `seaborn` statistical plotting library.'
             % axis)
    deltas = 0.5 * np.diff(coord, axis=axis)
    if deltas.size == 0:
        deltas = np.array(0.0)
    first = np.take(coord, [0], axis=axis) - np.take(deltas, [0], axis=axis)
    last = np.take(coord, [-1], axis=axis) + np.take(deltas, [-1], axis=axis)
    trim_last = tuple(slice(None, -1) if n == axis else slice(None) for n in
        range(coord.ndim))
    return np.concatenate([first, coord[trim_last] + deltas, last], axis=axis)