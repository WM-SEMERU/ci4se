def item_attribute(self, f=None, name=None):

    def decorator(func):
        attr_name = name or func.__name__
        if attr_name.startswith('_'):
            raise RuntimeError(
                'Invalid dynamic item attribute name -- should not start with an underscore'
                )
        self.__item_attributes[attr_name] = func
        return func
    if f is None:
        return decorator
    else:
        return decorator(f)