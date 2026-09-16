def set_global_config(path_dict_or_stream):
    path = None
    mapping = None
    stream = None
    global _config_file_path
    global _config_cache
    if isinstance(path_dict_or_stream, string_types):
        path = path_dict_or_stream
        if _config_file_path and _config_file_path != path:
            raise Exception(
                'set_global_config(%r) differs from %r, consider calling clear_global_config first'
                 % (path, _config_file_path))
        _config_file_path = path
        stream = open(path)
    elif isinstance(path_dict_or_stream, collections.Mapping):
        mapping = path_dict_or_stream
    elif hasattr(path_dict_or_stream, 'read'):
        stream = path_dict_or_stream
    else:
        raise Exception(
            'set_global_config(%r) instead of a path, mapping object, or stream open for reading'
             % path_dict_or_stream)
    if stream is not None:
        mapping = yaml.load(stream, Loader)
    _config_cache = mapping
    return _config_cache