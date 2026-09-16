def json_data(self, instance, default=None):
    value = self.get(instance)
    if value:
        return value.output
    return value