def json_data(self, instance, default=None):
    value = self.get(instance)
    if not value:
        return ''
    if callable(value):
        value = value()
    return api.to_iso_date(value, default=default)