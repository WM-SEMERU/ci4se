def _check_connection(self):
    if self.tcp_disconnect_timer + 2 * self.reconnect_timeout < time.time():
        self.tcp_disconnect_timer = time.time()
        raise OSError('No response from {}. Disconnecting'.format(self.
            server_address))
    if self.tcp_check_timer + self.reconnect_timeout >= time.time():
        return
    msg = Message().modify(child_id=255, type=self.const.MessageType.
        internal, sub_type=self.const.Internal.I_VERSION)
    self.add_job(msg.encode)
    self.tcp_check_timer = time.time()