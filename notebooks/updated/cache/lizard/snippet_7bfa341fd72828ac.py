async def generate_refresh_token(self, request, user):
    refresh_token = await utils.call(self.config.generate_refresh_token())
    user_id = await self._get_user_id(user)
    await utils.call(self.store_refresh_token, user_id=user_id,
        refresh_token=refresh_token, request=request)
    return refresh_token