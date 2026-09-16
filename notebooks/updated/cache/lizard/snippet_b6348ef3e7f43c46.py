def remove(self, id_equipamento, id_egrupo):
    if not is_valid_int_param(id_egrupo):
        raise InvalidParameterError(
            'O identificador do grupo de equipamento é inválido ou não foi informado.'
            )
    if not is_valid_int_param(id_equipamento):
        raise InvalidParameterError(
            'O identificador do equipamento é inválido ou não foi informado.')
    url = 'egrupo/equipamento/' + str(id_equipamento) + '/egrupo/' + str(
        id_egrupo) + '/'
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml)