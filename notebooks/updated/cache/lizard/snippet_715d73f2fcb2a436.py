def link_to_storage(self, sensor_log):
    if self.walker is not None:
        self._sensor_log.destroy_walker(self.walker)
        self.walker = None
    self.walker = sensor_log.create_walker(self.selector)
    self._sensor_log = sensor_log