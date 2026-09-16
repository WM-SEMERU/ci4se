def file_links(items, opts=None):
    result = []
    kwargs = get_kwargs_for_file_link(opts)
    for item in items:
        if isinstance(item, FileNode):
            result.append(get_file_link(item, **kwargs))
        else:
            result.append(file_links(item, kwargs))
    return result