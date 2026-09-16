async def on_raw_731(self, message):
    for nick in message.params[1].split(','):
        self._destroy_user(nick, monitor_override=True)
        await self.on_user_offline(nickname)