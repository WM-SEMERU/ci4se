def get_size(self, value=None):
    if value is None:
        return sum(cls_val.get_size(obj_val) for obj_val, cls_val in self.
            _get_attributes())
    elif isinstance(value, type(self)):
        return value.get_size()
    else:
        msg = '{} is not an instance of {}'.format(value, type(self).__name__)
        raise PackException(msg)