def ack(self, items):
    for item in items:
        time_to_ack = item.time_to_ack
        if time_to_ack is not None:
            self._manager.ack_histogram.add(time_to_ack)
    ack_ids = [item.ack_id for item in items]
    request = types.StreamingPullRequest(ack_ids=ack_ids)
    self._manager.send(request)
    self.drop(items)