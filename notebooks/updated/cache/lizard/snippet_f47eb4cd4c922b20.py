def queue(self):
    entry = self._proto.commandQueueEntry
    if entry.HasField('queueName'):
        return entry.queueName
    return None