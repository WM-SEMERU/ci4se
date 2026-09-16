def create(cls, serializable_instance):
    if not Serializable.is_serializable(serializable_instance):
        raise ValueError(
            'Can only create pickles for Serializable objects, given {} of type {}'
            .format(serializable_instance, type(serializable_instance).
            __name__))
    return cls(unpickle_func=_unpickle_serializable, args=(type(
        serializable_instance), serializable_instance._asdict()))