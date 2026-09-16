async def _set_get_started(self):
    page = self.settings()
    if 'get_started' in page:
        payload = page['get_started']
    else:
        payload = {'action': 'get_started'}
    await self._send_to_messenger_profile(page, {'get_started': {'payload':
        ujson.dumps(payload)}})
    logger.info('Get started set for page %s', page['page_id'])