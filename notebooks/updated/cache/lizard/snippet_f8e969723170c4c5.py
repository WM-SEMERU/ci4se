def get_single_key(d):
    assert len(d
        ) == 1, 'Single-item dict must have just one item, not %d.' % len(d)
    return next(six.iterkeys(d))