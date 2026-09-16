def _from_dict(cls, _dict):
    args = {}
    xtra = _dict.copy()
    if 'entity' in _dict:
        args['entity'] = _dict.get('entity')
        del xtra['entity']
    else:
        raise ValueError(
            "Required property 'entity' not present in RuntimeEntity JSON")
    if 'location' in _dict:
        args['location'] = _dict.get('location')
        del xtra['location']
    else:
        raise ValueError(
            "Required property 'location' not present in RuntimeEntity JSON")
    if 'value' in _dict:
        args['value'] = _dict.get('value')
        del xtra['value']
    else:
        raise ValueError(
            "Required property 'value' not present in RuntimeEntity JSON")
    if 'confidence' in _dict:
        args['confidence'] = _dict.get('confidence')
        del xtra['confidence']
    if 'metadata' in _dict:
        args['metadata'] = _dict.get('metadata')
        del xtra['metadata']
    if 'groups' in _dict:
        args['groups'] = [CaptureGroup._from_dict(x) for x in _dict.get(
            'groups')]
        del xtra['groups']
    args.update(xtra)
    return cls(**args)