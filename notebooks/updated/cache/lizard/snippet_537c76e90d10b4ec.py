def all(self, as_dict=False, as_ordereddict=False):
    rows = list(self)
    if as_dict:
        return [r.as_dict() for r in rows]
    elif as_ordereddict:
        return [r.as_dict(ordered=True) for r in rows]
    return rows