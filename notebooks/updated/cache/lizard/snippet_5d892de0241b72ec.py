def process(self):
    for filename, warnings in self.warnings.iteritems():
        self.fileCounts[filename] = {}
        fc = self.fileCounts[filename]
        fc['warning_count'] = len(warnings)
        fc['warning_breakdown'] = self._warnCount(warnings)
        self.warningCounts = self._warnCount(warnings, warningCount=self.
            warningCounts)