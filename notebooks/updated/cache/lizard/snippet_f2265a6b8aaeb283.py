def bigtable_viewers(self):
    result = set()
    for member in self._bindings.get(BIGTABLE_VIEWER_ROLE, ()):
        result.add(member)
    return frozenset(result)