def filter(self, resource_manager, **params):
    m = self.resolve(resource_manager.resource_type)
    client = local_session(self.session_factory).client(m.service)
    enum_op, path, extra_args = m.enum_spec
    if extra_args:
        params.update(extra_args)
    parent_type, parent_key, annotate_parent = m.parent_spec
    parents = self.manager.get_resource_manager(parent_type)
    parent_ids = [p[parents.resource_type.id] for p in parents.resources()]
    existing_param = parent_key in params
    if not existing_param and len(parent_ids) == 0:
        return []
    if existing_param:
        return self._invoke_client_enum(client, enum_op, params, path)
    results = []
    for parent_id in parent_ids:
        merged_params = self.get_parent_parameters(params, parent_id,
            parent_key)
        subset = self._invoke_client_enum(client, enum_op, merged_params,
            path, retry=self.manager.retry)
        if annotate_parent:
            for r in subset:
                r[self.parent_key] = parent_id
        if subset and self.capture_parent_id:
            results.extend([(parent_id, s) for s in subset])
        elif subset:
            results.extend(subset)
    return results