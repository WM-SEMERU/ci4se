def merge(self, other):
    if not isinstance(other, BuildFileAliases):
        raise TypeError('Can only merge other BuildFileAliases, given {0}'.
            format(other))

    def merge(*items):
        merged = {}
        for item in items:
            merged.update(item)
        return merged
    targets = merge(self.target_types, self.target_macro_factories, other.
        target_types, other.target_macro_factories)
    objects = merge(self.objects, other.objects)
    context_aware_object_factories = merge(self.
        context_aware_object_factories, other.context_aware_object_factories)
    return BuildFileAliases(targets=targets, objects=objects,
        context_aware_object_factories=context_aware_object_factories)