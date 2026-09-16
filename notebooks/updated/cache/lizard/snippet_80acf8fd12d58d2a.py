def min(a, axis=None):
    axes = _normalise_axis(axis, a)
    assert axes is not None and len(axes) == 1
    return _Aggregation(a, axes[0], _MinStreamsHandler,
        _MinMaskedStreamsHandler, a.dtype, {})