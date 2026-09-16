def get_field_type(cls, name):
    python_type = cls._get_field_python_type(cls.model, name)
    if python_type in _COLUMN_FIELD_MAP:
        field_class = _COLUMN_FIELD_MAP[python_type]
        return field_class(name)
    return BaseField(name)