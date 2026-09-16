def get_prefix_source(cls):
    try:
        return cls.override_prefix()
    except AttributeError:
        if hasattr(cls, '_prefix_source'):
            return cls.site + cls._prefix_source
        else:
            return cls.site