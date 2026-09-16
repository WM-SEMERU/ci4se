def __parameter_descriptor(self, subfield_list):
    descriptor = {}
    final_subfield = subfield_list[-1]
    if all(subfield.required for subfield in subfield_list):
        descriptor['required'] = True
    descriptor['type'] = self.__field_to_parameter_type(final_subfield)
    default = self.__parameter_default(final_subfield)
    if default is not None:
        descriptor['default'] = default
    if any(subfield.repeated for subfield in subfield_list):
        descriptor['repeated'] = True
    enum_descriptor = self.__parameter_enum(final_subfield)
    if enum_descriptor is not None:
        descriptor['enum'] = enum_descriptor
    return descriptor