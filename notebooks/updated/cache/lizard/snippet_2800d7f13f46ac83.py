async def get_users(self):
    cmd = 'get_users'
    url = self.base_url + cmd
    users = []
    try:
        async with async_timeout.timeout(8, loop=self._loop):
            response = await self._session.get(url)
        logger('Status from Tautulli: ' + str(response.status))
        all_user_data = await response.json()
        for user in all_user_data['response']['data']:
            if user['username'] != 'Local':
                users.append(user['username'])
        self.tautulli_users = users
        logger(self.tautulli_users)
    except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror,
        AttributeError) as error:
        msg = 'Can not load data from Tautulli: {} - {}'.format(url, error)
        logger(msg, 40)