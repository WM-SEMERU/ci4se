def _transfer_data(self, remote_path, data):
    if isinstance(data, dict):
        data = jsonify(data)
    if not isinstance(data, bytes):
        data = to_bytes(data, errors='surrogate_or_strict')
    LOG.debug('_transfer_data(%r, %s ..%d bytes)', remote_path, type(data),
        len(data))
    self._connection.put_data(remote_path, data)
    return remote_path