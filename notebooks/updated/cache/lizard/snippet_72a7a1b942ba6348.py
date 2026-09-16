def consume(self, limit=None):
    for total_message_count in count():
        if limit and total_message_count >= limit:
            raise StopIteration
        if not self.channel.is_open:
            raise StopIteration
        self.channel.conn.drain_events()
        yield True