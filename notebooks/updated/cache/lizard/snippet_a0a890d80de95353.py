def getAnalysisKeywords(self):
    analyses = []
    for rows in self.getRawResults().values():
        for row in rows:
            analyses = list(set(analyses + row.keys()))
    return analyses