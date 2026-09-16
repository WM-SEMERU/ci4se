def _new_sensor_reading(self, sensor_value):
    if not self._active and not self._enabled:
        return
    if self._dimensions > 1:
        for dimension in range(0, self._dimensions):
            value = sensor_value[dimension]
            self._sub_sensors[dimension]._new_sensor_reading(value)
    else:
        self._sensor_value.value = sensor_value