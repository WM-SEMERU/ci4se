def get(self, attr_name, *args):
    if not isinstance(attr_name, six.string_types):
        raise TypeError('attr_name must be a str.')
    if '-' in attr_name:
        attr_name = attr_name.replace('-', '_')
    parent_attr = self
    attr = getattr(parent_attr, attr_name, None)
    for arg in args:
        if not isinstance(arg, six.string_types):
            raise TypeError(
                'each additional argument must be a string. {0} was not a string'
                .format(arg))
        if hasattr(parent_attr, arg):
            parent_attr = getattr(parent_attr, arg)
            if hasattr(parent_attr, attr_name):
                attr = getattr(parent_attr, attr_name)
    else:
        pass
    return attr