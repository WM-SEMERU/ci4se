def static_rev(path):
    static_path = StaticNode.handle_simple(path)
    if is_debug():
        return dev_url(static_path)
    return production_url(path, static_path)