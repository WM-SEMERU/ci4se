def add_corpus(self, customization_id, corpus_name, corpus_file,
    allow_overwrite=None, **kwargs):
    if customization_id is None:
        raise ValueError('customization_id must be provided')
    if corpus_name is None:
        raise ValueError('corpus_name must be provided')
    if corpus_file is None:
        raise ValueError('corpus_file must be provided')
    headers = {}
    if 'headers' in kwargs:
        headers.update(kwargs.get('headers'))
    sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'add_corpus')
    headers.update(sdk_headers)
    params = {'allow_overwrite': allow_overwrite}
    form_data = {}
    form_data['corpus_file'] = None, corpus_file, 'text/plain'
    url = '/v1/customizations/{0}/corpora/{1}'.format(*self.
        _encode_path_vars(customization_id, corpus_name))
    response = self.request(method='POST', url=url, headers=headers, params
        =params, files=form_data, accept_json=True)
    return response