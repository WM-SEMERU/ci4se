def common_properties(self, build_request, requirements):
    assert isinstance(build_request, property_set.PropertySet)
    assert isinstance(requirements, property_set.PropertySet)
    free_unconditional = []
    other = []
    for p in requirements.all():
        if (p.feature.free and not p.condition and p.feature.name !=
            'conditional'):
            free_unconditional.append(p)
        else:
            other.append(p)
    other = property_set.create(other)
    key = build_request, other
    if key not in self.request_cache:
        self.request_cache[key] = self.__common_properties2(build_request,
            other)
    return self.request_cache[key].add_raw(free_unconditional)