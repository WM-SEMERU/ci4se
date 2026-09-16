def load_from_dict(self, data: dict, overwrite: bool=True):
    if data is None or data == {}:
        return False
    if isinstance(data, list) or isinstance(data, tuple):
        if len(data[0]) != 2:
            raise exc.LoaderException('Cannot load data with length {}'.
                format(len(data[0])))
        items = data
    elif isinstance(data, dict) or isinstance(data, self.__class__):
        items = data.items()
    else:
        raise exc.LoaderException('Cannot load data of type {}'.format(type
            (data)))
    for key, item in items:
        assert isinstance(key, str)
        if hasattr(self, key) and not overwrite:
            continue
        if self.safe_load:
            if key.startswith('__') or key in ['dump', 'items', 'keys',
                'values', 'iter_list', 'load_from_dict', 'iter_list_dump',
                'parsed', 'safe_load']:
                key = 'unsafe_' + key
        if '.' in key:
            key = key.replace('.', '_')
        if isinstance(item, dict):
            ncfg = ConfigKey()
            ncfg.load_from_dict(item)
            setattr(self, key, ncfg)
        elif isinstance(item, list):
            nlst = self.iter_list(item)
            setattr(self, key, nlst)
        else:
            setattr(self, key, item)
    self.parsed = True