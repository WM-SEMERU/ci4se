def ClaimRecords(self, limit=10000, timeout='30m', start_time=None,
    record_filter=lambda x: False, max_filtered=1000):
    if not self.locked:
        raise aff4.LockError('Queue must be locked to claim records.')
    with data_store.DB.GetMutationPool() as mutation_pool:
        return mutation_pool.QueueClaimRecords(self.urn, self.rdf_type,
            limit=limit, timeout=timeout, start_time=start_time,
            record_filter=record_filter, max_filtered=max_filtered)