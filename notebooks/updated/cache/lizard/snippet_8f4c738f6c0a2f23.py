def __non_body_parameter_descriptor(self, param):
    descriptor = {}
    descriptor['name'] = param.name
    param_type, param_format = self.__field_to_parameter_type_and_format(param)
    if param.required:
        descriptor['required'] = True
    descriptor['type'] = param_type
    if param_format:
        descriptor['format'] = param_format
    default = self.__parameter_default(param)
    if default is not None:
        descriptor['default'] = default
    if param.repeated:
        descriptor['repeated'] = True
    enum_descriptor = self.__parameter_enum(param)
    if enum_descriptor is not None:
        descriptor['enum'] = enum_descriptor
    return descriptor