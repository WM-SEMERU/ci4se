def clear_to_reset(self, config_vars):
    super(SensorGraphSubsystem, self).clear_to_reset(config_vars)
    self.graph.clear()
    if not self.persisted_exists:
        return
    for node in self.persisted_nodes:
        self.graph.add_node(node)
    for streamer_desc in self.persisted_streamers:
        streamer = streamer_descriptor.parse_string_descriptor(streamer_desc)
        self.graph.add_streamer(streamer)
    for stream, reading in self.persisted_constants:
        self._sensor_log.push(stream, reading)
    self.enabled = True
    for index, value in self.streamer_acks.items():
        self._seek_streamer(index, value)