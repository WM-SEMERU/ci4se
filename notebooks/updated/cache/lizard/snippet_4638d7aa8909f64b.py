def _open_script_interface(self, connection_id, callback):
    try:
        context = self.connections.get_context(connection_id)
    except ArgumentError:
        callback(connection_id, self.id, False,
            'Could not find connection information')
        return
    success = HighSpeedChar in context['services'][TileBusService]
    reason = None
    if not success:
        reason = 'Could not find high speed streaming characteristic'
    callback(connection_id, self.id, success, reason)