def authenticate_redirect(self, callback_uri=None, ask_for=['name', 'email',
    'language', 'username']):
    callback_uri = callback_uri or request.url
    args = self._openid_args(callback_uri, ax_attrs=ask_for)
    return redirect(self._OPENID_ENDPOINT + ('&' if '?' in self.
        _OPENID_ENDPOINT else '?') + urllib.urlencode(args))