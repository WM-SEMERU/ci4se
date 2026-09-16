def remove(self, id_vlan):
    if not is_valid_int_param(id_vlan):
        raise InvalidParameterError('Parameter id_vlan is invalid. Value: ' +
            id_vlan)
    url = 'vlan/' + str(id_vlan) + '/remove/'
    code, xml = self.submit(None, 'DELETE', url)
    return self.response(code, xml)