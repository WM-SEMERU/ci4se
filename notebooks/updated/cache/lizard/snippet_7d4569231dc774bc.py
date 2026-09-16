def runSearchFeatureSets(self, request):
    return self.runSearchRequest(request, protocol.SearchFeatureSetsRequest,
        protocol.SearchFeatureSetsResponse, self.featureSetsGenerator)