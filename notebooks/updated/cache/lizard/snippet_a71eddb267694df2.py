async def read(self, n=None):
    if self._streamed:
        return b''
    buffer = []
    async for body in self:
        buffer.append(body)
    return b''.join(buffer)