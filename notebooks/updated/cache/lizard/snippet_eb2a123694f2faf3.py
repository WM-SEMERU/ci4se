def getAnalysisRequests(self, **kwargs):
    brains = self.getAnalysisRequestsBrains(**kwargs)
    return [b.getObject() for b in brains]