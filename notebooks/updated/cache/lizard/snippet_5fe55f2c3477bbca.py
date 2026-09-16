def add_all_link_done_callback(self, callback):
    _LOGGER.debug('Added new callback %s ', callback)
    self._cb_load_all_link_db_done.append(callback)