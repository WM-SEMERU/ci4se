def caseinsensitive(cls):
    if not issubclass(cls, Enum):
        raise TypeError(
            'caseinsensitive decorator can only be applied to subclasses of enum.Enum'
            )
    enum_options = getattr(cls, PYCKSON_ENUM_OPTIONS, {})
    enum_options[ENUM_CASE_INSENSITIVE] = True
    setattr(cls, PYCKSON_ENUM_OPTIONS, enum_options)
    return cls