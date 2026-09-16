def scan(self, string):
    return list(self._scanner_to_matches(self.pattern.scanner(string), self
        .run))