def _handle_config(self, data):
    self.room.config.update(data)
    self.conn.enqueue_data('config', data)