def read_string(self, key, embedded=True):
    data = None
    if key is not None:
        key_type = self.variable_type(key)
        data = self.db.read(key.strip())
        if data is not None:
            try:
                data = json.loads(data)
                if embedded:
                    data = self.read_embedded(data, key_type)
                if data is not None:
                    data = '{}'.format(data)
            except ValueError as e:
                err = 'Failed loading JSON data ({}). Error: ({})'.format(data,
                    e)
                self.tcex.log.error(err)
    else:
        self.tcex.log.warning('The key field was None.')
    return data