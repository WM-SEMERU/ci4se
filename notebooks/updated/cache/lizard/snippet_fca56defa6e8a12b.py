def request(self, request):
    if request is None:
        raise ValueError('Invalid value for `request`, must not be `None`')
    if request is not None and not re.search(
        '^(?:[A-Za-z0-9+\\/]{4})*(?:[A-Za-z0-9+\\/]{2}==|[A-Za-z0-9+\\/]{3}=)?$'
        , request):
        raise ValueError(
            'Invalid value for `request`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\\/]{4})*(?:[A-Za-z0-9+\\/]{2}==|[A-Za-z0-9+\\/]{3}=)?$/`'
            )
    self._request = request