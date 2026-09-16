async def mgmt_request_async(self, message, operation, op_type=None, node=
    None, callback=None, **kwargs):
    while not await self.auth_complete_async():
        await asyncio.sleep(0.05)
    response = await asyncio.shield(self._session.mgmt_request_async(
        message, operation, op_type=op_type, node=node, callback=callback,
        encoding=self._encoding, debug=self._debug_trace, **kwargs))
    return response