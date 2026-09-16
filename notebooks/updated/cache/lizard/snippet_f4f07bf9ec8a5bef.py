async def has_started(self):
    timeout = False
    auth_in_progress = False
    if self._handler._connection.cbs:
        timeout, auth_in_progress = (await self._handler._auth.
            handle_token_async())
    if timeout:
        raise EventHubError('Authorization timeout.')
    if auth_in_progress:
        return False
    if not await self._handler._client_ready_async():
        return False
    return True