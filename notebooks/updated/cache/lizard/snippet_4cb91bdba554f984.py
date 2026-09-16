def render_request(self, sort=True):
    if not sort:
        return '; '.join(cookie.render_request() for cookie in self.values())
    return '; '.join(sorted(cookie.render_request() for cookie in self.
        values()))