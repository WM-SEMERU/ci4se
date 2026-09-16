def firmware_updates(self, firmware_updates):
    if firmware_updates is None:
        raise ValueError(
            'Invalid value for `firmware_updates`, must not be `None`')
    if firmware_updates is not None and firmware_updates < 0:
        raise ValueError(
            'Invalid value for `firmware_updates`, must be a value greater than or equal to `0`'
            )
    self._firmware_updates = firmware_updates