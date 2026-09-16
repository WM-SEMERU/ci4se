def inserir(self, id_user, id_group):
    if not is_valid_int_param(id_user):
        raise InvalidParameterError(
            'The identifier of User is invalid or was not informed.')
    if not is_valid_int_param(id_group):
        raise InvalidParameterError(
            'The identifier of Group is invalid or was not informed.')
    url = 'usergroup/user/' + str(id_user) + '/ugroup/' + str(id_group
        ) + '/associate/'
    code, xml = self.submit(None, 'PUT', url)