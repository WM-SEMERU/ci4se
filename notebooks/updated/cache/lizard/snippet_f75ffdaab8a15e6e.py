def widget_from_iterable(o):
    if isinstance(o, (list, dict)):
        return Dropdown(options=o)
    elif isinstance(o, Mapping):
        return Dropdown(options=list(o.items()))
    else:
        return Dropdown(options=list(o))