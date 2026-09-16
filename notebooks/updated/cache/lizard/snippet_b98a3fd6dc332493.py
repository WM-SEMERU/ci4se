def connect_to_another_user(self, user, password, token=None, is_public=False):
    return QubellPlatform.connect(self._router.base_url, user, password,
        token, is_public)