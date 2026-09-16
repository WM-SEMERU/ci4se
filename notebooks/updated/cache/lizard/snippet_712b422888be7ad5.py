def extended_status_request(self):
    self._status_received = False
    user_data = Userdata({'d1': self.group, 'd2': 0})
    cmd = ExtendedSend(self._address, COMMAND_EXTENDED_GET_SET_0X2E_0X00,
        userdata=user_data)
    cmd.set_checksum()
    self._send_method(cmd, self._status_message_received, True)