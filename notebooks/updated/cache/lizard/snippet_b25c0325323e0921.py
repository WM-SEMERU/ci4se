def list_objects(self, container, limit=None, marker=None, prefix=None,
    delimiter=None, end_marker=None, full_listing=False):
    if full_listing:
        return container.list_all(prefix=prefix)
    return container.list(limit=limit, marker=marker, prefix=prefix,
        delimiter=delimiter, end_marker=end_marker)