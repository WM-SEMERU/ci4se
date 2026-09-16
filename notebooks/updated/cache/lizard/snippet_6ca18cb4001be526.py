def _undo_save(self, datastreams, logMessage=None):
    return [ds for ds in datastreams if self.dscache[ds].undo_last_save(
        logMessage)]