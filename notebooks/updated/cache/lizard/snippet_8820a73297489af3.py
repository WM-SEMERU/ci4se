def fingerprint(self):
    return self.parse_fingerprint(self.cmdline) or self.read_metadata_by_name(
        self.name, self.FINGERPRINT_KEY)