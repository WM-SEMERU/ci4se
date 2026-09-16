async def _read_messages(self):
    while not self._stopped and self._websocket is not None:
        async for message in self._websocket:
            if message.type == aiohttp.WSMsgType.TEXT:
                payload = message.json()
                event = payload.pop('type', 'Unknown')
                self._dispatch_event(event, data=payload)
            elif message.type == aiohttp.WSMsgType.ERROR:
                break