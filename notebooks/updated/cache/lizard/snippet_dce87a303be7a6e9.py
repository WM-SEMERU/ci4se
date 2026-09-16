async def flush(self, request: BernardRequest):
    if self._acq and 'callback_query' in self._update:
        try:
            cbq_id = self._update['callback_query']['id']
        except KeyError:
            pass
        else:
            await self.platform.call('answerCallbackQuery', **await self.
                _acq.serialize(cbq_id))
    return await super(TelegramResponder, self).flush(request)