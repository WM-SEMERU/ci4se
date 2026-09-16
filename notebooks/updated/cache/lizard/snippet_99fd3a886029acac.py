def get_db_prep_value(self, value, connection, prepared=False):
    if isinstance(value, basestring):
        return value
    return json.dumps(value, **self.dump_kwargs)