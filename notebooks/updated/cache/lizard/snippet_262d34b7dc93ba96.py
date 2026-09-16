def getReferenceAnalysesService(self, service_uid):
    analyses = []
    for analysis in self.objectValues('ReferenceAnalysis'):
        if analysis.getServiceUID() == service_uid:
            analyses.append(analysis)
    return analyses