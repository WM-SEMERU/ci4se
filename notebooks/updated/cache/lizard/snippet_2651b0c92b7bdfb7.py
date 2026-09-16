def poll(self):
    queue_empty = self.server.get_queue_empty_exception()
    try:
        packets = [self.queue.get(timeout=self.server.ping_timeout)]
        self.queue.task_done()
    except queue_empty:
        raise exceptions.QueueEmpty()
    if packets == [None]:
        return []
    while True:
        try:
            packets.append(self.queue.get(block=False))
            self.queue.task_done()
        except queue_empty:
            break
    return packets