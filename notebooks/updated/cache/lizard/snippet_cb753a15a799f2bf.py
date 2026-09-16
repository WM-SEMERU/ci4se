def coerce(self, value):
    if isinstance(value, dict):
        value = [value]
    if not isiterable_notstring(value):
        value = [value]
    return [coerce_single_instance(self.lookup_field, v) for v in value]