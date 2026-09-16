def _set_section(self, section):
    if self.section != section:
        if self.section > section:
            raise dns.exception.FormError
        self.section = section