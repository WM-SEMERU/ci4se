def reset(self, clear=False):
    if self._executing:
        self._executing = False
        self._request_info['execute'] = {}
    self._reading = False
    self._highlighter.highlighting_on = False
    if clear:
        self._control.clear()
        if self._display_banner:
            if self.kernel_banner:
                self._append_plain_text(self.kernel_banner)
            self._append_plain_text(self.banner)
    self._show_interpreter_prompt()