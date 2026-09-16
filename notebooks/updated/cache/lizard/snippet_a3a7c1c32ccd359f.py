async def reset_state(self, *, chat: typing.Union[str, int, None]=None,
    user: typing.Union[str, int, None]=None, with_data: typing.Optional[
    bool]=True):
    chat, user = self.check_address(chat=chat, user=user)
    await self.set_state(chat=chat, user=user, state=None)
    if with_data:
        await self.set_data(chat=chat, user=user, data={})