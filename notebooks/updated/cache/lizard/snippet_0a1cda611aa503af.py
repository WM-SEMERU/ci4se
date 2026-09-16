def info(self, message, domain=None):
    if domain is None:
        domain = self.extension_name
    info(message, domain)