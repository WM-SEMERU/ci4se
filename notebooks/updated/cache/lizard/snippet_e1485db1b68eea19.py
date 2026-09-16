def validate_parent_id(self, key, parent_id):
    id_ = getattr(self, 'id', None)
    if id_ is not None and parent_id is not None:
        assert id_ != parent_id, 'Can not be attached to itself.'
    return parent_id