def get(self, context):
    if self.get_options().recursive:
        requested_targets = context.targets(exclude_scopes=Scope(self.
            get_options().exclude_scopes))
    else:
        requested_targets = list(context.target_roots)
    expanded_targets = list(requested_targets)
    for t in requested_targets:
        expanded_targets.extend(context.build_graph.get_all_derivatives(t.
            address))
    return tuple(sorted([t for t in expanded_targets if isinstance(t,
        JvmTarget) and t.has_sources('.java')], key=lambda t: t.address.spec))