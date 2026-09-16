def class_string(self, klass):
    if isinstance(klass, string_types):
        return klass
    return klass.__module__ + '.' + klass.__name__