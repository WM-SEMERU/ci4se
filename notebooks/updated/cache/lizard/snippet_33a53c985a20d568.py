def _init_message(self):
    try:
        self.message = compat.text_type(self.error)
    except UnicodeError:
        try:
            self.message = str(self.error)
        except UnicodeEncodeError:
            self.message = self.error.args[0]
    if not isinstance(self.message, compat.text_type):
        self.message = compat.text_type(self.message, 'ascii', 'replace')