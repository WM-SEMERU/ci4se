async def user_info(self, loop=None, **kwargs):
    if not self.user_info_url:
        raise NotImplementedError(
            'The provider doesnt support user_info method.')
    data = await self.request('GET', self.user_info_url, loop=loop, **kwargs)
    user = User(**dict(self.user_parse(data)))
    return user, data