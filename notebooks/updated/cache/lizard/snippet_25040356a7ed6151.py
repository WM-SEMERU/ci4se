async def fetch_widget(self, guild_id):
    data = await self.http.get_widget(guild_id)
    return Widget(state=self._connection, data=data)