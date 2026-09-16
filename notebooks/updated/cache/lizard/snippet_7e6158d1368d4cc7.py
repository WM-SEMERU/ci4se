def _replies(self, *args, **kwargs):
    reply_msg = make_reply(*args, **kwargs)
    if self._server:
        self._server._log('\t%d\t<-- %r' % (self.client_port, reply_msg))
    reply_bytes = reply_msg.reply_bytes(self)
    self._client.sendall(reply_bytes)