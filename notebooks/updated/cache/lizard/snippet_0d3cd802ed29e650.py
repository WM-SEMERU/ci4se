def __add_parameter(self, param, path_parameters, params):
    if not isinstance(param, messages.MessageField):
        if param.name in path_parameters:
            descriptor = self.__path_parameter_descriptor(param)
        else:
            descriptor = self.__query_parameter_descriptor(param)
        params.append(descriptor)
    else:
        for subfield_list in self.__field_to_subfields(param):
            qualified_name = '.'.join(subfield.name for subfield in
                subfield_list)
            if qualified_name in path_parameters:
                descriptor = self.__path_parameter_descriptor(subfield_list[-1]
                    )
                descriptor['required'] = True
                params.append(descriptor)