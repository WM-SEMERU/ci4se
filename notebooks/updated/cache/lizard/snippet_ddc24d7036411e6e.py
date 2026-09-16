async def _retreive_websocket_info(self):
    if self._web_client is None:
        self._web_client = WebClient(token=self.token, base_url=self.
            base_url, ssl=self.ssl, proxy=self.proxy, run_async=True, loop=
            self._event_loop, session=self._session)
    self._logger.debug('Retrieving websocket info.')
    if self.connect_method in ['rtm.start', 'rtm_start']:
        resp = await self._web_client.rtm_start()
    else:
        resp = await self._web_client.rtm_connect()
    url = resp.get('url')
    if url is None:
        msg = 'Unable to retreive RTM URL from Slack.'
        raise client_err.SlackApiError(message=msg, response=resp)
    return url, resp.data