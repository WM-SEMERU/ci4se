def find_ip4_by_id(self, id_ip):
    if not is_valid_int_param(id_ip):
        raise InvalidParameterError(
            'Ip identifier is invalid or was not informed.')
    url = 'ip/get/' + str(id_ip) + '/'
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml)