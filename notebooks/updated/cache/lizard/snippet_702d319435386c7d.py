def createSummary(self, log):
    warnings = self.obs.warnings
    errors = []
    if warnings:
        self.addCompleteLog('%d Warnings' % len(warnings), '\n'.join(warnings))
    if errors:
        self.addCompleteLog('%d Errors' % len(errors), '\n'.join(errors))