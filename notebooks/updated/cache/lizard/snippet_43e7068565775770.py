def alter(self, id_filter, name, description):
    if not is_valid_int_param(id_filter):
        raise InvalidParameterError(
            'The identifier of Filter is invalid or was not informed.')
    filter_map = dict()
    filter_map['name'] = name
    filter_map['description'] = description
    url = 'filter/' + str(id_filter) + '/'
    code, xml = self.submit({'filter': filter_map}, 'PUT', url)
    return self.response(code, xml)