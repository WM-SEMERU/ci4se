def user_getfield(self, field, access_token=None):
    info = self.user_getinfo([field], access_token)
    return info.get(field)