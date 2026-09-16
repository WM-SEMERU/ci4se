async def prepare(self, request):
    if request.method != 'GET':
        raise HTTPMethodNotAllowed(request.method, ['GET'])
    if not self.prepared:
        writer = await super().prepare(request)
        self._loop = request.app.loop
        self._ping_task = self._loop.create_task(self._ping())
        self.enable_chunked_encoding()
        return writer
    elif request.protocol.transport is None:
        raise asyncio.CancelledError()