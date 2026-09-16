def printSysLog(self, logString):
    if zvmsdklog.LOGGER.getloglevel() <= logging.DEBUG:
        if self.daemon == '':
            self.logger.debug(self.requestId + ': ' + logString)
        else:
            self.daemon.logger.debug(self.requestId + ': ' + logString)
    if self.captureLogs is True:
        self.results['logEntries'].append(self.requestId + ': ' + logString)
    return