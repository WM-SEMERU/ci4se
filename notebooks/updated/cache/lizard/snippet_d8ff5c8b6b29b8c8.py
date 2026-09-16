def first_where(pred, iterable, default=None):
    return next(six.moves.filter(pred, iterable), default)