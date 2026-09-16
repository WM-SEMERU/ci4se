def _x_tune_ok(self, channel_max, frame_max, heartbeat):
    args = AMQPWriter()
    args.write_short(channel_max)
    args.write_long(frame_max)
    args.write_short(heartbeat or 0)
    self._send_method((10, 31), args)
    self._wait_tune_ok = False