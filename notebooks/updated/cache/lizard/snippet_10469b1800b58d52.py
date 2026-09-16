def from_api_repr(cls, resource):
    config = cls(resource['sourceFormat'])
    for optcls in _OPTION_CLASSES:
        opts = resource.get(optcls._RESOURCE_NAME)
        if opts is not None:
            config._options = optcls.from_api_repr(opts)
            break
    config._properties = copy.deepcopy(resource)
    return config