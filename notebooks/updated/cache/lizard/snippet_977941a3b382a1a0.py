async def get_all_leases(self):
    lease_futures = []
    partition_ids = await self.host.partition_manager.get_partition_ids_async()
    for partition_id in partition_ids:
        lease_futures.append(self.get_lease_async(partition_id))
    return lease_futures