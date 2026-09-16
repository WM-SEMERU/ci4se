def _from_dict(cls, _dict):
    args = {}
    if 'name' in _dict:
        args['name'] = _dict.get('name')
    else:
        raise ValueError(
            "Required property 'name' not present in ClassifierResult JSON")
    if 'classifier_id' in _dict:
        args['classifier_id'] = _dict.get('classifier_id')
    else:
        raise ValueError(
            "Required property 'classifier_id' not present in ClassifierResult JSON"
            )
    if 'classes' in _dict:
        args['classes'] = [ClassResult._from_dict(x) for x in _dict.get(
            'classes')]
    else:
        raise ValueError(
            "Required property 'classes' not present in ClassifierResult JSON")
    return cls(**args)