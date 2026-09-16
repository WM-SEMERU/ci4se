def with_default_context(cls, use_empty_init=False, global_default_factory=None
    ):
    if use_empty_init:
        if global_default_factory is not None:
            warnings.warn(
                'Either factory or use_empty_init should be set. Assuming use_empty_init=True.'
                )
        global_default_factory = lambda : cls()
    class_attrs = dict(_default_stack=DefaultStack(),
        _global_default_factory=global_default_factory)
    class_attrs.update(cls.__dict__)
    return type(cls.__name__, (cls, _DefaultContextMixin), class_attrs)