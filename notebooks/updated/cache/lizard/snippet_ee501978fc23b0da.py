def delete_classifier(self, classifier_id, **kwargs):
    if classifier_id is None:
        raise ValueError('classifier_id must be provided')
    headers = {}
    if 'headers' in kwargs:
        headers.update(kwargs.get('headers'))
    sdk_headers = get_sdk_headers('watson_vision_combined', 'V3',
        'delete_classifier')
    headers.update(sdk_headers)
    params = {'version': self.version}
    url = '/v3/classifiers/{0}'.format(*self._encode_path_vars(classifier_id))
    response = self.request(method='DELETE', url=url, headers=headers,
        params=params, accept_json=True)
    return response