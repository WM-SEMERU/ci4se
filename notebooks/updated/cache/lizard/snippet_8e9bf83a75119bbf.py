def unexpected_disconnect(self, conn_or_internal_id):
    data = {'id': conn_or_internal_id}
    action = ConnectionAction('force_disconnect', data, sync=False)
    self._actions.put(action)