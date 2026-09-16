def pop(self, key, *args):
    assert isinstance(key, basestring)
    return dict.pop(self, key.lower(), *args)