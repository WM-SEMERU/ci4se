def certs(self):
    return dict([(a, e) for a, e in self.entries.items() if isinstance(e,
        TrustedCertEntry)])