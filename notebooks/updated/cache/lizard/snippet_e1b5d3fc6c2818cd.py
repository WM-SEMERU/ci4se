def ReleaseRecords(cls, ids, token):
    with data_store.DB.GetMutationPool() as mutation_pool:
        mutation_pool.QueueReleaseRecords(ids)