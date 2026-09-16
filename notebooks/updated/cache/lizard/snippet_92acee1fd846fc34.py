def generate_oauth_signature(self, params, url):
    if 'oauth_signature' in params.keys():
        del params['oauth_signature']
    base_request_uri = quote(url, '')
    params = self.sorted_params(params)
    params = self.normalize_parameters(params)
    query_params = ['{param_key}%3D{param_value}'.format(param_key=key,
        param_value=value) for key, value in params.items()]
    query_string = '%26'.join(query_params)
    string_to_sign = '%s&%s&%s' % (self.method, base_request_uri, query_string)
    consumer_secret = str(self.consumer_secret)
    if self.version not in ['v1', 'v2']:
        consumer_secret += '&'
    hash_signature = HMAC(consumer_secret.encode(), str(string_to_sign).
        encode(), sha256).digest()
    return b64encode(hash_signature).decode('utf-8').replace('\n', '')