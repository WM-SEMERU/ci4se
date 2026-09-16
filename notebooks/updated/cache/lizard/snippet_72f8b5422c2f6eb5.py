def expect_session(self, protocol_factory, peer_jid, sid):

    def on_done(fut):
        del self._expected_sessions[sid, peer_jid]
    _, fut = self._expected_sessions[sid, peer_jid
        ] = protocol_factory, asyncio.Future()
    fut.add_done_callback(on_done)
    return fut