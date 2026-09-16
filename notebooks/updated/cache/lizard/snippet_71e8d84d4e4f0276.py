def getuserinfo(self, default=None, encoding='utf-8', errors='strict'):
    userinfo = self.userinfo
    if userinfo is None:
        return default
    else:
        return uridecode(userinfo, encoding, errors)