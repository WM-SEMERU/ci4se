async def post(self, path, data={}, send_raw=False, **params):
    url = self.get_url(path, **params)
    jstr = json.dumps(data)
    for i in range(self.tries + 1):
        try:
            if send_raw:
                resp = await self.session.post(url, data=data, timeout=self
                    .timeout)
            else:
                resp = await self.session.post(url, data=jstr, timeout=self
                    .timeout)
            if await self._process_resp(resp):
                return resp
            else:
                continue
        except aiohttp.ClientConnectionError:
            if i >= self.tries:
                raise aiohttp.ClientConnectionError(
                    'Emby server is probably down')