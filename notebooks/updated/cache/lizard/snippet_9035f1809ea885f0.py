def get_loader(config_uri, protocols=None):
    config_uri = parse_uri(config_uri)
    requested_scheme = config_uri.scheme
    matched_loaders = find_loaders(requested_scheme, protocols=protocols)
    if len(matched_loaders) < 1:
        raise LoaderNotFound(requested_scheme, protocols=protocols)
    if len(matched_loaders) > 1:
        raise MultipleLoadersFound(requested_scheme, matched_loaders,
            protocols=protocols)
    loader_info = matched_loaders[0]
    loader = loader_info.load(config_uri)
    return loader