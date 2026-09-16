def getAuthenticator(self, service_request):
    auth = service_request.service.getAuthenticator(service_request)
    if auth is None:
        return self.authenticator
    return auth