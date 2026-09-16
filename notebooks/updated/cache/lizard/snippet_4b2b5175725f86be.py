def _required_attr(self, attr, key):
    assert isinstance(attr, dict)
    if key not in attr:
        raise AttributeError('Required attribute {} not found.'.format(key))
    return attr[key]