def runSearchRnaQuantificationSets(self, request):
    return self.runSearchRequest(request, protocol.
        SearchRnaQuantificationSetsRequest, protocol.
        SearchRnaQuantificationSetsResponse, self.
        rnaQuantificationSetsGenerator)