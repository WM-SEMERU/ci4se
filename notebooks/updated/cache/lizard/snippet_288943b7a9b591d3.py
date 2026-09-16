def declarations(cls, extra_defs=None):
    warnings.warn(
        'Factory.declarations is deprecated; use Factory._meta.pre_declarations instead.'
        , DeprecationWarning, stacklevel=2)
    decls = cls._meta.pre_declarations.as_dict()
    decls.update(extra_defs or {})
    return decls