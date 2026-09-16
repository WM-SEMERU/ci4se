async def on_raw_join(self, message):
    await super().on_raw_join(message)
    nick, metadata = self._parse_user(message.source)
    channels = message.params[0].split(',')
    if self.is_same_nick(self.nickname, nick):
        if 'WHOX' in self._isupport and self._isupport['WHOX']:
            await self.rawmsg('WHO', ','.join(channels), '%tnurha,{id}'.
                format(id=WHOX_IDENTIFIER))
    else:
        pass