def getRealmUserPassword(self, realmname, username, environ):
    return self.user_manager.get_user_api_key(username, create=True)