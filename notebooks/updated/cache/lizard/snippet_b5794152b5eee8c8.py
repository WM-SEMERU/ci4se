def decode_conjure_bean_type(cls, obj, conjure_type):
    deserialized = {}
    for python_arg_name, field_definition in conjure_type._fields().items():
        field_identifier = field_definition.identifier
        if field_identifier not in obj or obj[field_identifier] is None:
            cls.check_null_field(obj, deserialized, python_arg_name,
                field_definition)
        else:
            value = obj[field_identifier]
            field_type = field_definition.field_type
            deserialized[python_arg_name] = cls.do_decode(value, field_type)
    return conjure_type(**deserialized)