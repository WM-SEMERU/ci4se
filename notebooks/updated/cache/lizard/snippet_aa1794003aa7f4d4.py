def get_user_info(self, user_id, **kwargs):
    return GetUserInfo(settings=self.settings, **kwargs).call(user_id=
        user_id, **kwargs)