def _get_web_session(self):
    if isinstance(self.backend, MobileWebAuth):
        return self.backend.session
    elif self.backend.logged_on:
        sess = self.backend.get_web_session()
        if sess is None:
            raise RuntimeError(
                'Failed to get a web session. Try again in a few minutes')
        else:
            return sess
    else:
        raise RuntimeError('SteamClient instance is not connected')