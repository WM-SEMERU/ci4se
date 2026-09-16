def _route(self, attr, args, kwargs, **fkwargs):
    key = get_key(args, kwargs)
    return [crc32(str(key)) % len(self.cluster)]