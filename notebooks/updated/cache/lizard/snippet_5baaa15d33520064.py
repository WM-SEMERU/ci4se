def _from_dict(cls, _dict):
    args = {}
    if 'document_id' in _dict:
        args['document_id'] = _dict.get('document_id')
    if 'field' in _dict:
        args['field'] = _dict.get('field')
    if 'start_offset' in _dict:
        args['start_offset'] = _dict.get('start_offset')
    if 'end_offset' in _dict:
        args['end_offset'] = _dict.get('end_offset')
    if 'entities' in _dict:
        args['entities'] = [QueryEvidenceEntity._from_dict(x) for x in
            _dict.get('entities')]
    return cls(**args)