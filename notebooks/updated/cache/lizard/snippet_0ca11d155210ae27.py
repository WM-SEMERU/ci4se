async def api_get(self, url, params=None):
    request = None
    headers = DEFAULT_HEADERS.copy()
    headers.update({'Session-Token': self._token})
    try:
        with async_timeout.timeout(DEFAULT_TIMEOUT, loop=self._event_loop):
            request = await self._api_session.get(url, headers=headers,
                params=params)
        if request.status != 200:
            _LOGGER.error('Error fetching Eight data: %s', request.status)
            return None
        if 'application/json' in request.headers['content-type']:
            request_json = await request.json()
        else:
            _LOGGER.debug('Response was not JSON, returning text.')
            request_json = await request.text()
        return request_json
    except (aiohttp.ClientError, asyncio.TimeoutError, ConnectionRefusedError
        ) as err:
        _LOGGER.error('Error fetching Eight data. %s', err)
        return None