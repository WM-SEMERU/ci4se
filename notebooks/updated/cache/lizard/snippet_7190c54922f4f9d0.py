def delete(self, domain, type_name, search_command):
    return self._request(domain, type_name, search_command, 'DELETE', None)