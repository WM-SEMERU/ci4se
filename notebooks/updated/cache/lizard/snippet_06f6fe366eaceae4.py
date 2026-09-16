def is_serializable_type(type_):
    if not inspect.isclass(type_):
        return Serializable.is_serializable(type_)
    return issubclass(type_, Serializable) or hasattr(type_, '_asdict')