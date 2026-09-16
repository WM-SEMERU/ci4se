def register(cls, range_mixin):

    def decorator(range_set_mixin):
        cls.add(range_mixin, range_set_mixin)
        return range_set_mixin
    return decorator