def convert_multiple_sources_to_consumable_types(self, project, prop_set,
    sources):
    if __debug__:
        from .targets import ProjectTarget
        assert isinstance(project, ProjectTarget)
        assert isinstance(prop_set, property_set.PropertySet)
        assert is_iterable_typed(sources, virtual_target.VirtualTarget)
    if not self.source_types_:
        return list(sources)
    acceptable_types = set()
    for t in self.source_types_:
        acceptable_types.update(type.all_derived(t))
    result = []
    for source in sources:
        if source.type() not in acceptable_types:
            transformed = construct_types(project, None, self.source_types_,
                prop_set, [source])
            for t in transformed[1]:
                if t.type() in self.source_types_:
                    result.append(t)
            if not transformed:
                project.manager().logger().log(__name__,
                    '  failed to convert ', source)
        else:
            result.append(source)
    result = sequence.unique(result, stable=True)
    return result