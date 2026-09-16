def certificate(self, certificate):
    if certificate is not None and not re.search(
        '^(?:[A-Za-z0-9+\\/]{4})*(?:[A-Za-z0-9+\\/]{2}==|[A-Za-z0-9+\\/]{3}=)?$'
        , certificate):
        raise ValueError(
            'Invalid value for `certificate`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\\/]{4})*(?:[A-Za-z0-9+\\/]{2}==|[A-Za-z0-9+\\/]{3}=)?$/`'
            )
    self._certificate = certificate