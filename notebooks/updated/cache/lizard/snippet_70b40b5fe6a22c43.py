def _tuple_from_str(bbox):
    return tuple([float(s) for s in bbox.replace(',', ' ').split() if s])