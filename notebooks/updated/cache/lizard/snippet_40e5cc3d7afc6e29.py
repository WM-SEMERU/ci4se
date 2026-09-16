def purge(self, queue, nowait=True, ticket=None, cb=None):
    nowait = nowait and self.allow_nowait() and not cb
    args = Writer()
    args.write_short(ticket or self.default_ticket).write_shortstr(queue
        ).write_bit(nowait)
    self.send_frame(MethodFrame(self.channel_id, 50, 30, args))
    if not nowait:
        self._purge_cb.append(cb)
        return self.channel.add_synchronous_cb(self._recv_purge_ok)