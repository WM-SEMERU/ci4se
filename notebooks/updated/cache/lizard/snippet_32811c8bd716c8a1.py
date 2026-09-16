def methods(method_list):
    assert isinstance(method_list, list) and len(method_list) > 0

    def deco(handler):
        d = _HandleRequestDict()
        for m in method_list:
            d[m.upper()] = handler
        return d
    return deco