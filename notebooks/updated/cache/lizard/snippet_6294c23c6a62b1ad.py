def _get_config(self, host, port, unix_socket, auth, config_key):
    client = self._client(host, port, unix_socket, auth)
    if client is None:
        return None
    config_value = client.config_get(config_key)
    del client
    return config_value