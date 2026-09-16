def _get_cookie(self, name, domain):
    for c in self.session.cookies:
        if c.name == name and c.domain == domain:
            return c
    return None