def first(self, default=None, as_dict=False, as_ordereddict=False):
    try:
        record = self[0]
    except IndexError:
        if isexception(default):
            raise default
        return default
    if as_dict:
        return record.as_dict()
    elif as_ordereddict:
        return record.as_dict(ordered=True)
    else:
        return record