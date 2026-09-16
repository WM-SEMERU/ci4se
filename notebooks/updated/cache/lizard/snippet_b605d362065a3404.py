def add_grammar(self, customization_id, grammar_name, grammar_file,
    content_type, allow_overwrite=None, **kwargs):
    if customization_id is None:
        raise ValueError('customization_id must be provided')
    if grammar_name is None:
        raise ValueError('grammar_name must be provided')
    if grammar_file is None:
        raise ValueError('grammar_file must be provided')
    if content_type is None:
        raise ValueError('content_type must be provided')
    headers = {'Content-Type': content_type}
    if 'headers' in kwargs:
        headers.update(kwargs.get('headers'))
    sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'add_grammar')
    headers.update(sdk_headers)
    params = {'allow_overwrite': allow_overwrite}
    data = grammar_file
    url = '/v1/customizations/{0}/grammars/{1}'.format(*self.
        _encode_path_vars(customization_id, grammar_name))
    response = self.request(method='POST', url=url, headers=headers, params
        =params, data=data, accept_json=True)
    return response