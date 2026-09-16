def _send_status_0x01_request(self):
    status_command = StandardSend(self._address,
        COMMAND_LIGHT_STATUS_REQUEST_0X19_0X01)
    self._send_method(status_command, self._status_message_received)