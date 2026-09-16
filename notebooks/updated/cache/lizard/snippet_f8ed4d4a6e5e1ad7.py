def detector_voltage(self, channels=None):
    if channels is None:
        channels = self._channels
    channels = self._name_to_index(channels)
    if hasattr(channels, '__iter__') and not isinstance(channels, six.
        string_types):
        return [self._detector_voltage[ch] for ch in channels]
    else:
        return self._detector_voltage[channels]