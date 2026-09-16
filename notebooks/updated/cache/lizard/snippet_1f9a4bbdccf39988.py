def _process_media_status(self, data):
    self.status.update(data)
    self.logger.debug('Media:Received status %s', data)
    if self.status.media_session_id is None:
        self.session_active_event.clear()
    else:
        self.session_active_event.set()
    self._fire_status_changed()