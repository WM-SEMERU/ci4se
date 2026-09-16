def write_frame(self, frame_out):
    self.check_for_errors()
    self._connection.write_frame(self.channel_id, frame_out)