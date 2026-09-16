def disconnect_channel(self, destination_id):
    if destination_id in self._open_channels:
        try:
            self.send_message(destination_id, NS_CONNECTION, {MESSAGE_TYPE:
                TYPE_CLOSE, 'origin': {}}, no_add_request_id=True, force=True)
        except NotConnected:
            pass
        except Exception:
            self.logger.exception('[%s:%s] Exception', self.fn or self.host,
                self.port)
        self._open_channels.remove(destination_id)
        self.handle_channel_disconnected()