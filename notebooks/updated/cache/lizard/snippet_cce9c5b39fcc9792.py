def get(cls, resource_id, include_deactivated=False):
    if include_deactivated:
        resource = yield cls.view.first(key=resource_id, include_docs=True)
    else:
        resource = yield cls.active_view.first(key=resource_id,
            include_docs=True)
    parent = cls.parent_resource(**resource['doc'])
    raise Return(cls(parent=parent, **resource['value']))