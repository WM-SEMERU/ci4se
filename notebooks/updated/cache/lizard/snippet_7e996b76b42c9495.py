def query_extensions(self, extension_query, account_token=None,
    account_token_header=None):
    query_parameters = {}
    if account_token is not None:
        query_parameters['accountToken'] = self._serialize.query(
            'account_token', account_token, 'str')
    content = self._serialize.body(extension_query, 'ExtensionQuery')
    response = self._send(http_method='POST', location_id=
        'eb9d5ee1-6d43-456b-b80e-8a96fbc014b6', version='5.1-preview.1',
        query_parameters=query_parameters, content=content)
    return self._deserialize('ExtensionQueryResult', response)