async def receive_updates(self, request: Request):
    body = await request.read()
    try:
        content = ujson.loads(body)
    except ValueError:
        return json_response({'error': True, 'message':
            'Cannot decode body'}, status=400)
    logger.debug('Received from Telegram: %s', content)
    message = TelegramMessage(content, self)
    responder = TelegramResponder(content, self)
    await self._notify(message, responder)
    return json_response({'error': False})