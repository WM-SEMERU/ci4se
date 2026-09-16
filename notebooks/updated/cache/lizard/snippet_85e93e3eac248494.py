def add_streamer(self, streamer):
    if self._max_streamers is not None and len(self.streamers
        ) >= self._max_streamers:
        raise ResourceUsageError('Maximum number of streamers exceeded',
            max_streamers=self._max_streamers)
    streamer.link_to_storage(self.sensor_log)
    streamer.index = len(self.streamers)
    self.streamers.append(streamer)