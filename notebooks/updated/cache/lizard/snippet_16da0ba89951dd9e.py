def __get_doc_block_parts_wrapper(self):
    self.__get_doc_block_parts_source()
    helper = self._get_data_type_helper()
    parameters = list()
    for parameter_info in self._parameters:
        parameters.append({'parameter_name': parameter_info['name'],
            'python_type': helper.column_type_to_python_type(parameter_info
            ), 'data_type_descriptor': parameter_info[
            'data_type_descriptor'], 'description': self.
            __get_parameter_doc_description(parameter_info['name'])})
    self._doc_block_parts_wrapper['description'
        ] = self._doc_block_parts_source['description']
    self._doc_block_parts_wrapper['parameters'] = parameters