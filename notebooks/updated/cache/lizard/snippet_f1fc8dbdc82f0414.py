def parse_querystring(self, req, name, field):
    return core.get_value(req.params, name, field)