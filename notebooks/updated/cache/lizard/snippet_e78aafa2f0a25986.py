def from_json(cls, json):
    params = dict((str(k), v) for k, v in json.iteritems() if k in cls._PARAMS)
    if cls._OFFSET_PARAM in params:
        params[cls._OFFSET_PARAM] = base64.b64decode(params[cls._OFFSET_PARAM])
    return cls(**params)