def is_proxy(elt):
    if ismethod(elt):
        elt = get_method_function(elt)
    result = hasattr(elt, __PROXIFIED__)
    return result