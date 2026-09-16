def request_entity(self, request_entity):
    if request_entity is not None and len(request_entity) > 10000:
        raise ValueError(
            'Invalid value for `request_entity`, length must be less than or equal to `10000`'
            )
    self._request_entity = request_entity