def _handle_waited_log(self, event: dict):
    txn_hash = event['transactionHash']
    event_name = event['event']
    assert event_name in self.event_waiting
    assert txn_hash in self.event_waiting[event_name]
    self.event_count[event_name][txn_hash] += 1
    event_entry = self.event_waiting[event_name][txn_hash]
    if event_entry.count == self.event_count[event_name][txn_hash]:
        self.event_waiting[event_name].pop(txn_hash)
    if event_entry.callback:
        event_entry.callback(event)