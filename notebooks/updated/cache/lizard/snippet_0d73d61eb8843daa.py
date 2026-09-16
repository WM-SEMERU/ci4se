def fail(self, key, **kwargs):
    try:
        msg = self.error_messages[key]
    except KeyError:
        class_name = self.__class__.__name__
        msg = MISSING_ERROR_MESSAGE.format(class_name=class_name, key=key)
        raise AssertionError(msg)
    if isinstance(msg, str):
        msg = msg.format(**kwargs)
    raise exceptions.ValidationError(msg, self.field_name)