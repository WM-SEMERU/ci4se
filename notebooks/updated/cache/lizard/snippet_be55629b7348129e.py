def _valid_search(self, s):
    if isinstance(s, six.string_types):
        return lambda l: s in l
    elif isinstance(s, list) and len(s) > 0 and all(isinstance(w, six.
        string_types) for w in s):
        return lambda l: all(w in l for w in s)
    elif s is not None:
        raise TypeError(
            'Search items must be given as a string or a list of strings')