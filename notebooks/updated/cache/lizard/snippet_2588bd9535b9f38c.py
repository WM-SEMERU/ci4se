async def on_shutdown(self):
    await self._unregister_subscriptions()
    self._accepting = False
    for ws, _ in self._subscribers:
        await ws.close(code=aiohttp.WSCloseCode.GOING_AWAY, message=
            'Server shutdown')