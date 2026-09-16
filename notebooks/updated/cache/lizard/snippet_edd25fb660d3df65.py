def json(self, command, arguments, tags=None, id=None):
    result = self.sync(command, arguments, tags=tags, id=id)
    if result.level != 20:
        raise RuntimeError(
            'invalid result level, expecting json(20) got (%d)' % result.level)
    return json.loads(result.data)