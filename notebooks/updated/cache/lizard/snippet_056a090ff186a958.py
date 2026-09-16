def validate(data):
    text = data.get('text')
    if not isinstance(text, _string_types) or len(text) == 0:
        raise ValueError('text field is required and should not be empty')
    if 'markdown' in data and not type(data['markdown']) is bool:
        raise ValueError('markdown field should be bool')
    if 'attachments' in data:
        if not isinstance(data['attachments'], (list, tuple)):
            raise ValueError('attachments field should be list or tuple')
        for attachment in data['attachments']:
            if 'text' not in attachment and 'title' not in attachment:
                raise ValueError('text or title is required in attachment')
    return True