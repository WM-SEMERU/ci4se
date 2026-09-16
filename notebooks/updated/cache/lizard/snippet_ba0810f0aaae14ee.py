async def on_raw_433(self, message):
    if not self.registered:
        self._registration_attempts += 1
        if self._attempt_nicknames:
            await self.set_nickname(self._attempt_nicknames.pop(0))
        else:
            await self.set_nickname(self._nicknames[0] + '_' * (self.
                _registration_attempts - len(self._nicknames)))