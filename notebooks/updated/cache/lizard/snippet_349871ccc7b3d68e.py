def buscar_por_ip_ambiente(self, ip, id_environment):
    if not is_valid_int_param(id_environment):
        raise InvalidParameterError(
            'Environment identifier is invalid or was not informed.')
    if not is_valid_ip(ip):
        raise InvalidParameterError('IP is invalid or was not informed.')
    url = 'ip/' + str(ip) + '/ambiente/' + str(id_environment) + '/'
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml)