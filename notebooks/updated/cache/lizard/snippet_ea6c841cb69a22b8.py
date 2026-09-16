def to_serializable_value(self):
    return_dict = {}
    for name, field in self.__dict__.items():
        if isinstance(field, fields.Field):
            return_dict[name] = field.to_serializable_value()
    return return_dict