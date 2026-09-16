def __params_descriptor(self, message_type, request_kind, path, method_id):
    path_parameter_dict = self.__get_path_parameters(path)
    if not isinstance(message_type, resource_container.ResourceContainer):
        if path_parameter_dict:
            _logger.warning(
                'Method %s specifies path parameters but you are not using a ResourceContainer; instead, you are using %r. This will fail in future releases; please switch to using ResourceContainer as soon as possible.'
                , method_id, type(message_type))
        return self.__params_descriptor_without_container(message_type,
            request_kind, method_id, path)
    params = []
    if message_type.body_message_class != message_types.VoidMessage:
        params.append(self.__body_parameter_descriptor(method_id))
    params_message_type = message_type.parameters_message_class()
    for field_name, matched_path_parameters in path_parameter_dict.iteritems():
        field = params_message_type.field_by_name(field_name)
        self.__validate_path_parameters(field, matched_path_parameters)
    for field in sorted(params_message_type.all_fields(), key=lambda f: f.
        number):
        matched_path_parameters = path_parameter_dict.get(field.name, [])
        self.__add_parameter(field, matched_path_parameters, params)
    return params