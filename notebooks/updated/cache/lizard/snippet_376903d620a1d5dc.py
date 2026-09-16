def group_resources_by_type(resources):
    groups = defaultdict(list)
    for resource in resources:
        groups[getattr(resource, 'type')].append(resource)
    ordered = OrderedDict()
    for rtype, rtype_label in RESOURCE_TYPES.items():
        if groups[rtype]:
            ordered[rtype, rtype_label] = groups[rtype]
    return ordered