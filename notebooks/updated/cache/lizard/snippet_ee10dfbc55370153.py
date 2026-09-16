def dispatch_callback(self, items):
    if not self._manager.is_active:
        return
    batched_commands = collections.defaultdict(list)
    for item in items:
        batched_commands[item.__class__].append(item)
    _LOGGER.debug('Handling %d batched requests', len(items))
    if batched_commands[requests.LeaseRequest]:
        self.lease(batched_commands.pop(requests.LeaseRequest))
    if batched_commands[requests.ModAckRequest]:
        self.modify_ack_deadline(batched_commands.pop(requests.ModAckRequest))
    if batched_commands[requests.AckRequest]:
        self.ack(batched_commands.pop(requests.AckRequest))
    if batched_commands[requests.NackRequest]:
        self.nack(batched_commands.pop(requests.NackRequest))
    if batched_commands[requests.DropRequest]:
        self.drop(batched_commands.pop(requests.DropRequest))