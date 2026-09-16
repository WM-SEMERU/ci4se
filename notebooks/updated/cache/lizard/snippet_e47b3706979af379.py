async def delete_lease_async(self, lease):
    await self.host.loop.run_in_executor(self.executor, functools.partial(
        self.storage_client.delete_blob, self.lease_container_name, lease.
        partition_id, lease_id=lease.token))