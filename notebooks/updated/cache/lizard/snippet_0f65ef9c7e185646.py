def _make_key(relation):
    return _ReferenceKey(_lower(relation.database), _lower(relation.schema),
        _lower(relation.identifier))