def printAggregateJobStats(self, properties, childNumber):
    for job in self.jobsToReport:
        lf = lambda x: '%s:%s' % (x, str(x in properties))
        print('\t'.join(('JOB:%s' % job, 'LOG_FILE:%s' % job.
            logJobStoreFileID, 'TRYS_REMAINING:%i' % job.
            remainingRetryCount, 'CHILD_NUMBER:%s' % childNumber, lf(
            'READY_TO_RUN'), lf('IS_ZOMBIE'), lf('HAS_SERVICES'), lf(
            'IS_SERVICE'))))