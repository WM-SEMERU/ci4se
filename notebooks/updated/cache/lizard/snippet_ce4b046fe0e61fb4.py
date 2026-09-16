async def subscribe(self, topic):
    if self.socket_type not in {SUB, XSUB}:
        raise AssertionError('A %s socket cannot subscribe.' % self.
            socket_type.decode())
    self._subscriptions.append(topic)
    tasks = [asyncio.ensure_future(peer.connection.local_subscribe(topic),
        loop=self.loop) for peer in self._peers if peer.connection]
    if tasks:
        try:
            await asyncio.wait(tasks, loop=self.loop)
        finally:
            for task in tasks:
                task.cancel()