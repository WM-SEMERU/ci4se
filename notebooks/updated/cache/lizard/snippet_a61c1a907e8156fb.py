def get_messages(self, count=1, block=True, timeout=0.1):
    messages = []
    if timeout is not None:
        timeout += time.time()
    new_offsets = {}
    log.debug('getting %d messages', count)
    while len(messages) < count:
        block_time = timeout - time.time()
        log.debug('calling _get_message block=%s timeout=%s', block, block_time
            )
        block_next_call = block is True or block > len(messages)
        result = self._get_message(block_next_call, block_time,
            get_partition_info=True, update_offset=False)
        log.debug('got %s from _get_messages', result)
        if not result:
            if block_next_call and (timeout is None or time.time() <= timeout):
                continue
            break
        partition, message = result
        _msg = (partition, message) if self.partition_info else message
        messages.append(_msg)
        new_offsets[partition] = message.offset + 1
    self.offsets.update(new_offsets)
    self.count_since_commit += len(messages)
    self._auto_commit()
    log.debug('got %d messages: %s', len(messages), messages)
    return messages