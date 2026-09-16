def send_heartbeat(self):
    if self.connection._heartbeat:
        if time.time(
            ) >= self._last_heartbeat_send + 0.9 * self.connection._heartbeat:
            self.send_frame(HeartbeatFrame(self.channel_id))
            self._last_heartbeat_send = time.time()