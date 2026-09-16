def _convert(cls, other, ignoreScalars=False):
    if ignoreScalars:
        if isinstance(other, (int, float)):
            msg = 'unable to convert {} to {}'.format(other, cls.__name__)
            raise TypeError(msg)
    return cls(other) if not issubclass(type(other), cls) else other