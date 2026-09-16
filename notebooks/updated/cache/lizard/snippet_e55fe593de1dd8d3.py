def getClientUID(self):
    request = self.getRequest()
    if request:
        client = request.getClient()
        if client:
            return client.UID()