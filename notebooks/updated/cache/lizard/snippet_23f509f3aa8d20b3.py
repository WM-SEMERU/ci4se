async def persist_checkpoint_async(self, checkpoint,
    event_processor_context=None):
    _logger.debug('PartitionPumpCheckpointStart %r %r %r %r', self.host.
        guid, checkpoint.partition_id, checkpoint.offset, checkpoint.
        sequence_number)
    try:
        in_store_checkpoint = (await self.host.storage_manager.
            get_checkpoint_async(checkpoint.partition_id))
        if (not in_store_checkpoint or checkpoint.sequence_number >=
            in_store_checkpoint.sequence_number):
            if not in_store_checkpoint:
                _logger.info('persisting checkpoint %r', checkpoint.__dict__)
                await self.host.storage_manager.create_checkpoint_if_not_exists_async(
                    checkpoint.partition_id)
            self.lease.event_processor_context = event_processor_context
            if not await self.host.storage_manager.update_checkpoint_async(self
                .lease, checkpoint):
                _logger.error('Failed to persist checkpoint for partition: %r',
                    self.partition_id)
                raise Exception('failed to persist checkpoint')
            self.lease.offset = checkpoint.offset
            self.lease.sequence_number = checkpoint.sequence_number
        else:
            _logger.error(
                'Ignoring out of date checkpoint with offset %r/sequence number %r because '
                 +
                'current persisted checkpoint has higher offset %r/sequence number %r'
                , checkpoint.offset, checkpoint.sequence_number,
                in_store_checkpoint.offset, in_store_checkpoint.sequence_number
                )
            raise Exception('offset/sequenceNumber invalid')
    except Exception as err:
        _logger.error('PartitionPumpCheckpointError %r %r %r', self.host.
            guid, checkpoint.partition_id, err)
        raise
    finally:
        _logger.debug('PartitionPumpCheckpointStop %r %r', self.host.guid,
            checkpoint.partition_id)