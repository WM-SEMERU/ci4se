def _reset(self):
    self.log.info('Clearing the cache, resetting event offsets')
    self.raw_header = None
    self.event_offsets = []
    self.index = 0