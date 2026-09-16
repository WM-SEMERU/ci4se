def post(self, url, obj, content_type=JSON_CONTENT_TYPE, **kwargs):

    def retry_bad_nonce(f):
        f.trap(ServerError)
        if f.value.message.typ.split(':')[-1] == 'badNonce':
            self._nonces.clear()
            self._add_nonce(f.value.response)
            return self._post(url, obj, content_type, **kwargs)
        return f
    return self._post(url, obj, content_type, **kwargs).addErrback(
        retry_bad_nonce)