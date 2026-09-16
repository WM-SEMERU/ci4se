def add(self, val):
    if not isinstance(val, six.integer_types):
        raise ValueError('GaugePointLong only supports integer types')
    with self._value_lock:
        self.value += val