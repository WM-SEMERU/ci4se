def _config_win32_domain(self, domain):
    self.domain = dns.name.from_text(str(domain))