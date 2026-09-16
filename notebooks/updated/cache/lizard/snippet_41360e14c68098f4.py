def reserved_quota(self, reserved_quota):
    if reserved_quota is None:
        raise ValueError(
            'Invalid value for `reserved_quota`, must not be `None`')
    if reserved_quota is not None and reserved_quota < 0:
        raise ValueError(
            'Invalid value for `reserved_quota`, must be a value greater than or equal to `0`'
            )
    self._reserved_quota = reserved_quota