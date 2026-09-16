def generate(cls, partial_props=None):
    partial_props = partial_props or {}
    props = partial_props.copy()
    props.update(cls.DEFAULT_PROPERTIES)
    return cls(props)