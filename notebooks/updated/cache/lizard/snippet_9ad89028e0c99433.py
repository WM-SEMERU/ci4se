def _from_dict(cls, _dict):
    args = {}
    if 'expansions' in _dict:
        args['expansions'] = [Expansion._from_dict(x) for x in _dict.get(
            'expansions')]
    else:
        raise ValueError(
            "Required property 'expansions' not present in Expansions JSON")
    return cls(**args)