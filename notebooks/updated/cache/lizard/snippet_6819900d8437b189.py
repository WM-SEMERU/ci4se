def send_exit_status(self, status):
    m = Message()
    m.add_byte(chr(MSG_CHANNEL_REQUEST))
    m.add_int(self.remote_chanid)
    m.add_string('exit-status')
    m.add_boolean(False)
    m.add_int(status)
    self.transport._send_user_message(m)