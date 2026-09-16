def _is_null(self, value):
    if isinstance(value, six.string_types):
        if not len(value.strip()):
            return True
    return value is None