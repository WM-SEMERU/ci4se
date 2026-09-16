def fetch(self, id_, return_fields=None):
    game_params = {'id': id_}
    if return_fields is not None:
        self._validate_return_fields(return_fields)
        field_list = ','.join(return_fields)
        game_params['field_list'] = field_list
    response = self._query(game_params, direct=True)
    return response