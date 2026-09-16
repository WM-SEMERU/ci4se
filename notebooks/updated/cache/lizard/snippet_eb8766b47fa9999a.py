def consume(self, queue, consumer, consumer_tag='', no_local=False, no_ack=
    True, exclusive=False, nowait=True, ticket=None, cb=None):
    nowait = nowait and self.allow_nowait() and not cb
    if nowait and consumer_tag == '':
        consumer_tag = self._generate_consumer_tag()
    args = Writer()
    args.write_short(ticket or self.default_ticket).write_shortstr(queue
        ).write_shortstr(consumer_tag).write_bits(no_local, no_ack,
        exclusive, nowait).write_table({})
    self.send_frame(MethodFrame(self.channel_id, 60, 20, args))
    if not nowait:
        self._pending_consumers.append((consumer, cb))
        self.channel.add_synchronous_cb(self._recv_consume_ok)
    else:
        self._consumer_cb[consumer_tag] = consumer