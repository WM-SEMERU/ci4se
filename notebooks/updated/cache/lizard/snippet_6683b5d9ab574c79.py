def build_projection_kwargs(cls, source, mapping):
    return cls._map_arg_names(source, cls._default_attr_mapping + mapping)