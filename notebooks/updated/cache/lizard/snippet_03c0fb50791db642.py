def remover(self, id_direito):
    if not is_valid_int_param(id_direito):
        raise InvalidParameterError(
            'O identificador do direito grupo equipamento é inválido ou não foi informado.'
            )
    url = 'direitosgrupoequipamento/' + str(id_direito) + '/'
    code, xml = self.submit(None, 'DELETE', url)
    return self.response(code, xml)