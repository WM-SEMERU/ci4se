def createSessionForKey(self, key, user):
    PersistentSession(store=self.store, sessionKey=key, authenticatedAs=user)