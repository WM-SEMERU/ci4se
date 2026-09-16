def dict_contents(self, use_dict=None, as_class=None):
    if _debug:
        _log.debug('dict_contents use_dict=%r as_class=%r', use_dict, as_class)
    return str(self)