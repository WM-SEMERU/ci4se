def _has_no_pendings(self, statuses):
    return all(s != ClientBatchStatus.PENDING for s in statuses.values())