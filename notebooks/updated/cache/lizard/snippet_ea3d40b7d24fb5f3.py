def fetch_access_token(self, oauth_request):
    version = self._get_version(oauth_request)
    consumer = self._get_consumer(oauth_request)
    try:
        verifier = self._get_verifier(oauth_request)
    except Error:
        verifier = None
    token = self._get_token(oauth_request, 'request')
    self._check_signature(oauth_request, consumer, token)
    new_token = self.data_store.fetch_access_token(consumer, token, verifier)
    return new_token