async def close_async(self, reason):
    self.set_pump_status('Closing')
    try:
        await self.on_closing_async(reason)
        if self.processor:
            _logger.info('PartitionPumpInvokeProcessorCloseStart %r %r %r',
                self.host.guid, self.partition_context.partition_id, reason)
            await self.processor.close_async(self.partition_context, reason)
            _logger.info('PartitionPumpInvokeProcessorCloseStart %r %r',
                self.host.guid, self.partition_context.partition_id)
    except Exception as err:
        await self.process_error_async(err)
        _logger.error('%r %r %r', self.host.guid, self.partition_context.
            partition_id, err)
        raise err
    if reason == 'LeaseLost':
        try:
            _logger.info('Lease Lost releasing ownership')
            await self.host.storage_manager.release_lease_async(self.
                partition_context.lease)
        except Exception as err:
            _logger.error('%r %r %r', self.host.guid, self.
                partition_context.partition_id, err)
            raise err
    self.set_pump_status('Closed')