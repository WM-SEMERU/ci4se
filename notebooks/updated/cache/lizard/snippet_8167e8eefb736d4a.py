def parse_cookies(self, req, name, field):
    return core.get_value(req.COOKIES, name, field)