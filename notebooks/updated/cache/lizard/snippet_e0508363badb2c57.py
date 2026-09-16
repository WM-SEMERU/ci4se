def to_cls(self):
    try:
        if isinstance(self._to_cls, str):
            self._to_cls = fetch_entity_cls_from_registry(self._to_cls)
    except AssertionError:
        pass
    return self._to_cls