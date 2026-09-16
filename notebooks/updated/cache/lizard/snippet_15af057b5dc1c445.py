def remove_attribute_listener(self, attr_name, *args, **kwargs):
    attr_name = attr_name.upper()
    return super(Parameters, self).remove_attribute_listener(attr_name, *
        args, **kwargs)