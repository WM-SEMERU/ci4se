def remove(self, id_environment_vip):
    if not is_valid_int_param(id_environment_vip):
        raise InvalidParameterError(
            'The identifier of Environment VIP is invalid or was not informed.'
            )
    url = 'environmentvip/' + str(id_environment_vip) + '/'
    code, xml = self.submit(None, 'DELETE', url)
    return self.response(code, xml)