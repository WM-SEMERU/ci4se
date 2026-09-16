def with_(self, *relations):
    if not relations:
        return self
    eagers = self._parse_with_relations(list(relations))
    self._eager_load.update(eagers)
    return self