def catchup_subscriber(self, connection_id):
    with self._subscribers_cv:
        subscriber = self._subscribers[connection_id]
        last_known_block_id = subscriber.get_last_known_block_id()
        subscriptions = subscriber.subscriptions
    if last_known_block_id is not None:
        LOGGER.debug('Catching up Subscriber %s from %s', connection_id,
            last_known_block_id)
        for block_id in self.get_catchup_block_ids(last_known_block_id):
            events = self.get_events_for_block_id(block_id, subscriptions)
            event_list = EventList(events=events)
            self._send(connection_id, event_list.SerializeToString())