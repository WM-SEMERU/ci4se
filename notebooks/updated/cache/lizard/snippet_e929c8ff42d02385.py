def bool(self, item, default=None):
    try:
        item = self.__getattr__(item)
    except AttributeError as err:
        if default is not None:
            return default
        raise err
    if isinstance(item, (bool, int)):
        return bool(item)
    if isinstance(item, str) and item.lower() in ('n', 'no', 'false', 'f', '0'
        ):
        return False
    return True if item else False