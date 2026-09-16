def getIssuedBatchJobIDs(self):
    issuedJobs = set()
    for resultsFile in itervalues(self.resultsFiles):
        issuedJobs.update(self.getJobIDsForResultsFile(resultsFile))
    return list(issuedJobs)