def alterar(self, id_script, id_script_type, script, description, model=None):
    if not is_valid_int_param(id_script):
        raise InvalidParameterError(
            'The identifier of Script is invalid or was not informed.')
    script_map = dict()
    script_map['id_script_type'] = id_script_type
    script_map['script'] = script
    script_map['model'] = model
    script_map['description'] = description
    url = 'script/edit/' + str(id_script) + '/'
    code, xml = self.submit({'script': script_map}, 'PUT', url)
    return self.response(code, xml)