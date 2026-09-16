async def fetch_houses(self):
    try:
        async with self._websession.get(
            'https://production.plum.technology/v2/getHouses', headers=self
            .headers) as response:
            return await response.json()
    except IOError:
        print('Unable to login to Plum cloud servers.')
        sys.exit(5)