def _on_disconnect(self, result):
    success, _, context = self._parse_return(result)
    callback = context['callback']
    connection_id = context['connection_id']
    handle = context['handle']
    callback(connection_id, self.id, success, 'No reason given')
    self._remove_connection(handle)