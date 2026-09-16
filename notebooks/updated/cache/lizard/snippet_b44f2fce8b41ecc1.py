def expires(self):
    value = self._properties.get('expirationTime')
    if value is not None:
        return google.cloud._helpers._datetime_from_microseconds(1000.0 *
            float(value))