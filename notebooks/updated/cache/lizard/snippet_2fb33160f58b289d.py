def json(self, var, default=NOTSET):
    return self.get_value(var, cast=json.loads, default=default)