def _from_dict(cls, _dict):
    args = {}
    if 'document' in _dict:
        args['document'] = DocumentSentimentResults._from_dict(_dict.get(
            'document'))
    if 'targets' in _dict:
        args['targets'] = [TargetedSentimentResults._from_dict(x) for x in
            _dict.get('targets')]
    return cls(**args)