def reset_port_protection(self, id_or_uri, timeout=-1):
    uri = self._client.build_uri(id_or_uri) + '/resetportprotection'
    return self._client.update_with_zero_body(uri, timeout)