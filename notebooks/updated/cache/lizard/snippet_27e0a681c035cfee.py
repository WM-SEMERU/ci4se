def _from_dict(cls, _dict):
    args = {}
    if 'utterance_id' in _dict:
        args['utterance_id'] = _dict.get('utterance_id')
    else:
        raise ValueError(
            "Required property 'utterance_id' not present in UtteranceAnalysis JSON"
            )
    if 'utterance_text' in _dict:
        args['utterance_text'] = _dict.get('utterance_text')
    else:
        raise ValueError(
            "Required property 'utterance_text' not present in UtteranceAnalysis JSON"
            )
    if 'tones' in _dict:
        args['tones'] = [ToneChatScore._from_dict(x) for x in _dict.get(
            'tones')]
    else:
        raise ValueError(
            "Required property 'tones' not present in UtteranceAnalysis JSON")
    if 'error' in _dict:
        args['error'] = _dict.get('error')
    return cls(**args)