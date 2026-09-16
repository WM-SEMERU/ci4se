async def fetch_house(self, house_id):
    url = 'https://production.plum.technology/v2/getHouse'
    data = {'hid': house_id}
    return await self.__post(url, data)