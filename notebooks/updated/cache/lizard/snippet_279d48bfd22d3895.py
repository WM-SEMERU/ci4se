def _from_dict(cls, _dict):
    args = {}
    if 'trait_id' in _dict:
        args['trait_id'] = _dict.get('trait_id')
    else:
        raise ValueError(
            "Required property 'trait_id' not present in Trait JSON")
    if 'name' in _dict:
        args['name'] = _dict.get('name')
    else:
        raise ValueError("Required property 'name' not present in Trait JSON")
    if 'category' in _dict:
        args['category'] = _dict.get('category')
    else:
        raise ValueError(
            "Required property 'category' not present in Trait JSON")
    if 'percentile' in _dict:
        args['percentile'] = _dict.get('percentile')
    else:
        raise ValueError(
            "Required property 'percentile' not present in Trait JSON")
    if 'raw_score' in _dict:
        args['raw_score'] = _dict.get('raw_score')
    if 'significant' in _dict:
        args['significant'] = _dict.get('significant')
    if 'children' in _dict:
        args['children'] = [Trait._from_dict(x) for x in _dict.get('children')]
    return cls(**args)