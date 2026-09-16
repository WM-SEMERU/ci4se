def build_url(self):
    super(MailtoUrl, self).build_url()
    self.addresses = set()
    self.subject = None
    self.parse_addresses()
    if self.addresses:
        for addr in sorted(self.addresses):
            self.check_email_syntax(addr)
            if not self.valid:
                break
    elif not self.subject:
        self.add_warning(_(
            "No mail addresses or email subject found in `%(url)s'.") % {
            'url': self.url})