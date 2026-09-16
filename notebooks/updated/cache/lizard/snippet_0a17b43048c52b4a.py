def ListClients(self, request, timeout=None):
    return self._RetryLoop(lambda t: self._stub.ListClients(request, timeout=t)
        )