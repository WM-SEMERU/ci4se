def raw(self, raw):
    if raw is None:
        raise ValueError('Invalid value for `raw`, must not be `None`')
    if raw is not None and not re.search(
        '^(?:[A-Za-z0-9+\\/]{4})*(?:[A-Za-z0-9+\\/]{2}==|[A-Za-z0-9+\\/]{3}=)?$'
        , raw):
        raise ValueError(
            'Invalid value for `raw`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\\/]{4})*(?:[A-Za-z0-9+\\/]{2}==|[A-Za-z0-9+\\/]{3}=)?$/`'
            )
    self._raw = raw