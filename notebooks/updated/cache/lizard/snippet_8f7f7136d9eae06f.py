def syncItems(self, client=None, clientId=None):
    if client:
        clientId = client.clientIdentifier
    elif clientId is None:
        clientId = X_PLEX_IDENTIFIER
    data = self.query(SyncList.key.format(clientId=clientId))
    return SyncList(self, data)