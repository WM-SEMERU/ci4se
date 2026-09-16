async def acquire_lease_async(self, lease):
    retval = True
    new_lease_id = str(uuid.uuid4())
    partition_id = lease.partition_id
    try:
        if asyncio.iscoroutinefunction(lease.state):
            state = await lease.state()
        else:
            state = lease.state()
        if state == 'leased':
            if not lease.token:
                retval = False
            else:
                _logger.info('ChangingLease %r %r', self.host.guid, lease.
                    partition_id)
                await self.host.loop.run_in_executor(self.executor,
                    functools.partial(self.storage_client.change_blob_lease,
                    self.lease_container_name, partition_id, lease.token,
                    new_lease_id))
                lease.token = new_lease_id
        else:
            _logger.info('AcquiringLease %r %r', self.host.guid, lease.
                partition_id)
            lease.token = await self.host.loop.run_in_executor(self.
                executor, functools.partial(self.storage_client.
                acquire_blob_lease, self.lease_container_name, partition_id,
                self.lease_duration, new_lease_id))
        lease.owner = self.host.host_name
        lease.increment_epoch()
        retval = await self.update_lease_async(lease)
    except Exception as err:
        _logger.error('Failed to acquire lease %r %r %r', err, partition_id,
            lease.token)
        return False
    return retval