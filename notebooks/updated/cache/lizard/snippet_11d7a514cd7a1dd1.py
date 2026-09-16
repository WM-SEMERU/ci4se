def create_tc_entity(self, key, value):
    data = None
    if key is not None and value is not None:
        data = self.db.create(key.strip(), json.dumps(value))
    else:
        self.tcex.log.warning('The key or value field was None.')
    return data