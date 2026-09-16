def type(self, s, enter=False, clear=False):
    if clear:
        self.clear_text()
    self._uiauto.send_keys(s)
    if enter:
        self.keyevent('KEYCODE_ENTER')