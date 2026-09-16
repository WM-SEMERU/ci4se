def _as_document(self, partition):
    doc = super(self.__class__, self)._as_document(partition)
    doc['time_coverage'] = partition.time_coverage
    return doc