def list_connections(self, nome_interface, id_equipamento):
    if not is_valid_int_param(id_equipamento):
        raise InvalidParameterError(
            'Equipment identifier is none or was not informed.')
    if nome_interface is None or nome_interface == '':
        raise InvalidParameterError('Interface name was not informed.')
    nome_interface = nome_interface.replace('/', 's2it_replace')
    url = 'interface/' + urllib.quote(nome_interface) + '/equipment/' + str(
        id_equipamento) + '/'
    code, map = self.submit(None, 'GET', url)
    key = 'interfaces'
    return get_list_map(self.response(code, map, [key]), key)