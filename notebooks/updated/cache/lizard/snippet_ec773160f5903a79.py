def inject_include_info(self, path, config, include_type):
    if isinstance(config, list):
        config = config[0]
    ret = OrderedDict()
    ret[include_flag] = IncludeInfo(type=include_type, path=path)
    ret['config'] = config
    return ret