def one_or_none(self):
    if self._metadata is not None:
        raise RuntimeError(
            'Can not call `.one` or `.one_or_none` after stream consumption has already started.'
            )
    iterator = iter(self)
    try:
        answer = next(iterator)
    except StopIteration:
        return None
    try:
        next(iterator)
        raise ValueError('Expected one result; got more.')
    except StopIteration:
        return answer