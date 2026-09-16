def _from_dict(cls, _dict):
    args = {}
    if 'fonts' in _dict:
        args['fonts'] = [FontSetting._from_dict(x) for x in _dict.get('fonts')]
    return cls(**args)