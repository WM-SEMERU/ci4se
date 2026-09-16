def matchingAnalyseIndexes(self, tokenJson):
    matchingResults = self.matchingAnalyses(tokenJson)
    if matchingResults:
        indexes = [tokenJson[ANALYSIS].index(analysis) for analysis in
            matchingResults]
        return indexes
    return matchingResults