def mass_inform(self, msg):
    assert msg.mtype == Message.INFORM
    self._server.mass_send_message_from_thread(msg)