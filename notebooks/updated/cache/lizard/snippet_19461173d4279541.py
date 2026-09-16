def associate_environment_option_pool(self, id_option_pool, id_environment):
    if not is_valid_int_param(id_option_pool):
        raise InvalidParameterError(
            'The identifier of Option Pool is invalid or was not informed.')
    if not is_valid_int_param(id_environment):
        raise InvalidParameterError(
            'The identifier of Environment Pool is invalid or was not informed.'
            )
    url = 'api/pools/environment_options/save/'
    return self.post(url, {'option_id': id_option_pool, 'environment_id':
        id_environment})