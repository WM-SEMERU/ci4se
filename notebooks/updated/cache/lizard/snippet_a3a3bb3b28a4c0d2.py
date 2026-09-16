def _not_none(items):
    if not isinstance(items, (tuple, list)):
        items = items,
    return all(item is not _none for item in items)