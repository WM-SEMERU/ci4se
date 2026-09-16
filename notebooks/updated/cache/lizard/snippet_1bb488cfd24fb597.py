def flush_incoming(self):
    while True:
        try:
            stanza_obj = self._incoming_queue.get_nowait()
        except asyncio.QueueEmpty:
            break
        self._process_incoming(None, stanza_obj)