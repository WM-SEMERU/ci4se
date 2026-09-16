def GetUser(self, sid=None, uid=None, username=None):
    if sid:
        for user in self.users:
            if user.sid == sid:
                return user
        return None
    if uid:
        for user in self.users:
            if user.uid == uid:
                return user
    if username:
        for user in self.users:
            if user.username == username:
                if uid and user.uid and user.uid != uid:
                    return None
                else:
                    return user