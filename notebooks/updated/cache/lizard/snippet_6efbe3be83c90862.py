def resolve_name(view):
    if inspect.isfunction(view):
        return view.__name__
    if hasattr(view, 'url_name'):
        return view.url_name
    if isinstance(view, six.string_types):
        return view.split('.')[-1]
    return None