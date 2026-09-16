def RegisterPathSpec(cls, path_spec_type):
    type_indicator = path_spec_type.TYPE_INDICATOR
    if type_indicator in cls._path_spec_types:
        raise KeyError('Path specification type: {0:s} already set.'.format
            (type_indicator))
    cls._path_spec_types[type_indicator] = path_spec_type
    if getattr(path_spec_type, '_IS_SYSTEM_LEVEL', False):
        cls._system_level_type_indicators[type_indicator] = path_spec_type