def _send_string_clipboard(self, string: str, paste_command: model.SendMode):
    backup = self.clipboard.text
    if backup is None:
        logger.warning(
            'Tried to backup the X clipboard content, but got None instead of a string.'
            )
    self.clipboard.text = string
    try:
        self.mediator.send_string(paste_command.value)
    finally:
        self.ungrab_keyboard()
    self.__enqueue(self._restore_clipboard_text, backup)