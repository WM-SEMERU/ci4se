async def recv_message(self):
    message = await recv_message(self._stream, self._codec, self._recv_type)
    message, = await self._dispatch.recv_message(message)
    return message