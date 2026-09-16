def alterar(self, id_logicalenvironment, name):
    if not is_valid_int_param(id_logicalenvironment):
        raise InvalidParameterError(
            'The identifier of Logical Environment is invalid or was not informed.'
            )
    url = 'logicalenvironment/' + str(id_logicalenvironment) + '/'
    logical_environment_map = dict()
    logical_environment_map['name'] = name
    code, xml = self.submit({'logical_environment': logical_environment_map
        }, 'PUT', url)
    return self.response(code, xml)