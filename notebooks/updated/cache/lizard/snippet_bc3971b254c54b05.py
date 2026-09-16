def _from_dict(cls, _dict):
    args = {}
    xtra = _dict.copy()
    if 'intent' in _dict:
        args['intent'] = _dict.get('intent')
        del xtra['intent']
    else:
        raise ValueError(
            "Required property 'intent' not present in RuntimeIntent JSON")
    if 'confidence' in _dict:
        args['confidence'] = _dict.get('confidence')
        del xtra['confidence']
    else:
        raise ValueError(
            "Required property 'confidence' not present in RuntimeIntent JSON")
    args.update(xtra)
    return cls(**args)