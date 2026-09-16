def __params_order_descriptor(self, message_type, path, is_params_class=False):
    path_params = []
    query_params = []
    path_parameter_dict = self.__get_path_parameters(path)
    for field in sorted(message_type.all_fields(), key=lambda f: f.number):
        matched_path_parameters = path_parameter_dict.get(field.name, [])
        if not isinstance(field, messages.MessageField):
            name = field.name
            if name in matched_path_parameters:
                path_params.append(name)
            elif is_params_class and field.required:
                query_params.append(name)
        else:
            for subfield_list in self.__field_to_subfields(field):
                name = '.'.join(subfield.name for subfield in subfield_list)
                if name in matched_path_parameters:
                    path_params.append(name)
                elif is_params_class and field.required:
                    query_params.append(name)
    return path_params + sorted(query_params)