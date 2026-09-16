def _from_dict(cls, _dict):
    args = {}
    if 'customizations' in _dict:
        args['customizations'] = [LanguageModel._from_dict(x) for x in
            _dict.get('customizations')]
    else:
        raise ValueError(
            "Required property 'customizations' not present in LanguageModels JSON"
            )
    return cls(**args)