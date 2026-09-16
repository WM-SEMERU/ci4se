def on(self):
    on_command = ExtendedSend(self._address, COMMAND_LIGHT_ON_0X11_NONE,
        self._udata, cmd2=255)
    on_command.set_checksum()
    self._send_method(on_command, self._on_message_received)