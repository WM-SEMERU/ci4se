def _send_request(self, method, params=[], is_subscribe=False):
    self.next_id += 1
    req_id = self.next_id
    msg = {'id': req_id, 'method': method, 'params': params}
    if is_subscribe:
        waitQ = asyncio.Queue()
        self.subscriptions[method].append(waitQ)
    fut = asyncio.Future(loop=self.loop)
    self.inflight[req_id] = msg, fut
    if not self.protocol:
        logger.debug('Need to reconnect to server')

        async def connect_first():
            await self.reconnect()
            self.protocol.send_data(msg)
        self.loop.create_task(connect_first())
    else:
        self.protocol.send_data(msg)
    return fut if not is_subscribe else (fut, waitQ)